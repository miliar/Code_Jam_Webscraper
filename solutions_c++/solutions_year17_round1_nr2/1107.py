#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <algorithm>

void first_problem()
{
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {
        int rows, columns;
        std::cin >> rows >> columns;
        std::vector< std::vector<int> > cake;
        for (int j = 0; j < rows; ++j) {
            std::vector<int> row;
            std::string s;
            std::cin >> s;
            for (int k = 0; k < columns; ++k) {
                row.push_back(s[k]);
            }
            cake.push_back(row);
        }

        //find first row with char

        int cur_row = -1;

        bool found = false;
        for (int m = 0; m < cake.size(); ++m) {
            for (int j = 0; j < cake[m].size(); ++j) {
                if(cake[m][j] != '?')
                {
                    cur_row = m;
                    found = true;
                    break;
                }
            }
            if(found)
            {
                break;
            }
        }

        assert(cur_row != rows);

        int first_row = cur_row;

        while(cur_row < rows)
        {
            auto & row = cake[cur_row];
            int first_idx = -1;
            for (int j = 0; j < row.size(); ++j) {
                if(row[j] != '?')
                {
                    first_idx = j;
                    break;
                }
            }

            if(first_idx != -1)
            {
                int sign = row[first_idx];
                for (int j = 0; j < row.size(); ++j) {
                    if(row[j] != '?')
                    {
                        sign = row[j];
                    }
                    row[j] = sign;
                }
            }
            else
            {
                auto & prev_row = cake[cur_row - 1];
                for (int j = 0; j < row.size(); ++j) {
                    row[j] = prev_row[j];
                }
            }
            cur_row ++;
        }

        for (int l = 0; l < first_row; ++l) {
            for (int j = 0; j < columns; ++j) {
                cake[l][j] = cake[first_row][j];
            }
        }

        std::cout << "Case #" << i + 1 << ": " << "\n";

        for (int n = 0; n < rows; ++n) {
            for (int j = 0; j < columns; ++j) {
                std::cout << (char)cake[n][j];
            }
            std::cout << "\n";
        }

    }
}

struct Intervall{
    int first;
    int last;
    int ingredient;
    bool active = true;
};

struct Event{
    int time;
    size_t idx;
    bool start;

};

bool operator <(const Event& x, const Event& y) {
    return x.time < y.time or (x.time == y.time and x.start);
}

void second_problem()
{
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {

        int ingredients, pack;
        std::cin >> ingredients >> pack;

        std::vector<double> recipe;

        std::vector< std::vector<Intervall > > packings;

        for (int j = 0; j < ingredients; ++j) {
            double ing;
            std::cin >> ing;
            recipe.push_back(ing);
        }

        std::vector<Intervall> intervalls;
        std::vector<Event> events;

        for (int k = 0; k < ingredients; ++k) {
            for (int j = 0; j < pack; ++j) {
                double cur;
                std::cin >> cur;

                Intervall intervall;
                intervall.first = ceil(cur * 10.0/11.0 /recipe[k]);
                intervall.last  = floor(cur * 10.0 / 9.0 / recipe[k]);
                intervall.ingredient = k;
                if(intervall.first <= intervall.last)
                {
                    Event event_start;
                    event_start.time = intervall.first;
                    event_start.idx = intervalls.size();
                    event_start.start = true;
                    events.push_back(event_start);
                    Event event_finish;
                    event_finish.time = intervall.last;
                    event_finish.idx = intervalls.size();
                    event_finish.start = false;
                    events.push_back(event_finish);
                    intervalls.push_back(intervall);
                }

                std::sort(events.begin(), events.end());
            }
        }

        std::vector<std::vector<size_t>> interval_count(ingredients);

        int solution_count = 0;

        for (int l = 0; l < events.size(); ++l) {
            Event & event = events[l];
            Intervall & interval = intervalls[event.idx];
            if(event.start)
            {
                interval_count[interval.ingredient].push_back(event.idx);
                if(interval_count[interval.ingredient].size() == 1)
                {
                    bool all_active = true;
                    for (int j = 0; j < ingredients; ++j) {
                        if(interval_count[j].empty())
                        {
                            all_active = false;
                            break;
                        }
                    }

                    if(all_active)
                    {
                        //std::cout << "found solution at " << event.time << std::endl;
                        solution_count++;
                        for (int j = 0; j < ingredients; ++j) {
                           /* std::cout << "  idx " << j << " element " << interval_count[j][0] << " num active "
                                      << interval_count[j].size() << std::endl;*/
                            intervalls[interval_count[j][0]].active = false;
                            interval_count[j].erase(interval_count[j].begin());
                        }
                    }
                }
            }
            else
            {
                if(interval.active)
                {
                    //find intervall
                    for (int j = 0; j < interval_count[interval.ingredient].size(); ++j) {
                        if(interval_count[interval.ingredient][j] == event.idx)
                        {
                            interval_count[interval.ingredient].erase(interval_count[interval.ingredient].begin() + j);
                        }
                    }
                    interval.active = false;
                }
            }
        }


        std::cout << "Case #" << i + 1 << ": " << solution_count << "\n";

    }
}

int main() {
    second_problem();
    return 0;
}