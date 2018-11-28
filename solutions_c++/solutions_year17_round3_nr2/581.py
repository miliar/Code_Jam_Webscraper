#include <iostream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <limits>
#include <cassert>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>


long solve()
{
    return 0;
}

// activity: [start, end)
struct activity {
    long start;  // [0, 24*60=1440]
    long end;  // [0, 24*60=1440]
    size_t who;

    long duration() const {
        if (start <= end) {
            return end - start;
        } else {
            // spans midnight
            return (1440 - start) + end;
        }
    }
};

std::ostream& operator<<(std::ostream& stream, const activity& a) {
    if (a.who == 0) {
        stream << "C:";
    } else if (a.who == 1) {
        stream << "J:";
    } else {
        stream << "X:";
    }
    stream << "[" << a.start << "," << a.end << ")";
}

void run_test_case()
{
    size_t AC, AJ;
    std::cin >> AC >> AJ;

    std::vector<activity> ac;
    std::vector<activity> aj;
    std::vector<activity> as;


    long exchanges = 0;
    long free_time = 0; // time that can be freely allocated as an exchange must happen there
    long c_time = 0; // time that assigned to cameron
    long j_time = 0; // time that assigned to jamie
    std::vector<activity> free_chunks;

    /* std::vector<activity>* acj[] = {&ac, &aj}; */
    long* time[] = {&c_time, &j_time};

    std::vector<activity> c_fusable;
    std::vector<activity> j_fusable;
    std::vector<activity>* fusable[] = {&c_fusable, &j_fusable};

    for (size_t i = 0; i < AC; ++i) {
        activity a;
        std::cin >> a.start >> a.end;
        a.who = 0;
        ac.push_back(a);
        as.push_back(a);
        j_time += a.duration();
    }
    for (size_t i = 0; i < AJ; ++i) {
        activity a;
        std::cin >> a.start >> a.end;
        a.who = 1;
        aj.push_back(a);
        as.push_back(a);
        c_time += a.duration();
    }

    // sort activities by time
    std::sort(as.begin(), as.end(), [](activity x, activity y) { return x.start < y.start; });

    std::cerr << '\n';


    // count exchanges that *must* happen
    // examine each space between activities
    for (size_t i = 0; i < as.size(); ++i) {
        size_t j = (i + 1) % as.size();
        activity const& a1 = as[i];
        activity const& a2 = as[j];

        activity free_chunk;
        free_chunk.start = a1.end % 1440;
        free_chunk.end = a2.start;
        free_chunk.who = 1234;

        std::cerr << "Check " << a1 << " and " << a2 << ": ";
        if (a1.who != a2.who) {
            // exchange must happen
            exchanges += 1;
            free_time += free_chunk.duration();
            free_chunks.push_back(free_chunk);

            std::cerr << "must exchange";
            /* if (a1.start < a2.start) { */
            /*     free_time += a2.start - a1.end; */
            /* } */
            /* else { */
            /*     // midnight between */
            /*     free_time += (1440 - a1.end) + a2.start; */
            /* } */
        } else {
            // Try to fuse neighboring activities
            std::cerr << "might fuse";
            fusable[a1.who]->push_back(free_chunk);
            /* long& other_time = *time[1-a1.who]; */
            /* if (other_time + free_chunk.duration() <= 720) { */
            /*     // can fuse */
            /*     // mark this for later! */
            /*     fusable[a1.who]->push_back(free_chunk); */
            /*     /1* other_time += free_chunk.duration(); *1/ */
            /*     std::cerr << "fused"; */
            /* } else { */
            /*     // not possible, must handle later */
            /*     exchanges += 2; */
            /*     free_time += free_chunk.duration(); */
            /*     free_chunks.push_back(free_chunk); */
            /*     std::cerr << "cannot fuse (free: " << free_chunk << " with duration " << free_chunk.duration() << ")"; */
            /* } */
        }
        std::cerr << '\n';
    }

    for (int who = 0; who <= 1; ++who) {
        std::sort(fusable[who]->begin(), fusable[who]->end(), [](activity x, activity y) { return x.duration() < y.duration(); });
        long& other_time = *time[1-who];
        // fuse activities, starting with shortest in-between first
        for (activity const& fc : *(fusable[who])) {
            if (other_time + fc.duration() <= 720) {
                // fuse
                other_time += fc.duration();
                std::cerr << "fused at " << fc << "\n";
            } else {
                // cannot fuse
                exchanges += 2;
                free_time += fc.duration();
                std::cerr << "cannot fuse (free: " << fc << " with duration " << fc.duration() << ")\n";
            }
        }
    }

    std::cout << exchanges;
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
