#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <queue>
#include <assert.h>

struct city_t
{
    size_t horse_distance;
    size_t horse_speed;

    std::vector<long> distances;
};

std::vector<std::vector<double>> calculate_graph(std::vector<city_t> const & cities)
{
    std::vector<std::vector<double>> graph;
    for (size_t l = 0; l != cities.size(); ++l)
    {
        city_t sc = cities[l];

        std::vector<long> distances(cities.size(), -1);

        std::map<long, std::vector<size_t>> distances_queue;
        for (size_t k = 0; k != sc.distances.size(); ++k)
            if (sc.distances[k] != -1)
                distances_queue[sc.distances[k]].push_back(k);

        while (!distances_queue.empty() && distances_queue.begin()->first <= cities[l].horse_distance)
        {
            long distance = distances_queue.begin()->first;
            auto dcities = distances_queue.begin()->second;
            distances_queue.erase(distances_queue.begin());

            for (size_t ci: dcities)
            {
                if (distances[ci] == -1 || distances[ci] > distance)
                {
                    distances[ci] = distance;

                    city_t const & c = cities[ci];

                    for (size_t k = 0; k != distances.size(); ++k)
                        if (c.distances[k] != -1)
                            distances_queue[distance + c.distances[k]].push_back(k);
                }
            }
        }

        std::vector<double> times(cities.size(), std::numeric_limits<double>::infinity());
        for (size_t k = 0; k != cities.size(); ++k)
            if (distances[k] != -1 && distances[k] <= cities[l].horse_distance)
                times[k] = double(distances[k]) / cities[l].horse_speed;

        graph.push_back(times);
    }

    return graph;
}

double query(std::vector<std::vector<double>> const & graph, size_t start, size_t target)
{
    std::vector<double> distances(graph.size(), std::numeric_limits<double>::infinity());
    std::map<double, std::vector<size_t>> queue;
    for (size_t l = 0; l != graph.size(); ++l)
        queue[graph[start][l]].push_back(l);

    while (!queue.empty())
    {
        double t = queue.begin()->first;
        auto cities = queue.begin()->second;
        queue.erase(queue.begin());

        for (auto ci: cities)
        {
            if (distances[ci] > t)
            {
                distances[ci] = t;

                for (size_t k = 0; k != graph.size(); ++k)
                    if (k != ci)
                        queue[t + graph[ci][k]].push_back(k);
            }

            if (ci == target)
                return distances[ci];
        }
    }

    assert(0);

    return std::numeric_limits<double>::infinity();
}

std::vector<double> process(std::vector<city_t> const & cities, auto const & queries)
{
    auto graph = calculate_graph(cities);

    std::vector<double> res;
    for (auto v: queries)
        res.push_back(query(graph, v.first - 1, v.second - 1));

    return res;
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_c.txt");
    std::ofstream out("out_c.txt");

    out.setf(std::ios_base::fixed);
    out.precision(10);

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t N, Q;

        in >> N >> Q;

        std::vector<city_t> cities(N);
        for (size_t l = 0; l != N; ++l)
            in >> cities[l].horse_distance >> cities[l].horse_speed;

        for (size_t l = 0; l != N; ++l)
        {
            cities[l].distances.resize(N);
            for (size_t k = 0; k != N; ++k)
                in >> cities[l].distances[k];
        }

        std::vector<std::pair<size_t, size_t>> queries(Q);
        for (size_t l = 0; l != Q; ++l)
            in >> queries[l].first >> queries[l].second;

        auto res = process(cities, queries);
        out << "Case #" << i + 1 << ": ";
        for (auto v: res)
            out << v << " ";

        out << std::endl;
    }
}
