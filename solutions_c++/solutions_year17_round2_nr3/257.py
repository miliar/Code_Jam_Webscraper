#include <iostream>
#include <vector>
#include <limits>

int main() {
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {

        int N, Q;
        std::cin >> N >> Q;

        std::vector<double> horse_dist(N);
        std::vector<double> horse_speed(N);

        for (int j = 0; j < N; ++j) {
            std::cin >> horse_dist[j] >> horse_speed[j];
        }

        std::vector<std::vector< double > > lengths(N);
        for (int m = 0; m < N; ++m) {
            lengths[m].resize(N);
        }


        for (int k = 0; k < N; ++k) {
            for (int j = 0; j < N; ++j) {
                std::cin >> lengths[k][j];
            }
        }

        std::vector<size_t > U(Q);
        std::vector<size_t > V(Q);

        for (int l = 0; l < Q; ++l) {
            std::cin >> U[l] >> V[l];
        }

        //INPUT READ FINISH

        std::vector<std::vector<double > > real_dists;
        for (int k1 = 0; k1 < N; ++k1) {
            std::vector<double> r(N, 10e20);
            for (int j = 0; j < N; ++j) {
                if(lengths[k1][j] != -1)
                {
                    r[j] = lengths[k1][j];
                }
            }
            r[k1] = 0;
            real_dists.push_back(std::move(r));
        }
        
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                for (int l = 0; l < N; ++l) {
                        real_dists[k][l] = std::min(real_dists[k][l], real_dists[k][j] + real_dists[j][l]);
                }
            }
        }

        std::vector<std::vector< double >> times;
        for (int i1 = 0; i1 < N; ++i1) {
            std::vector<double> time_i(N, 10e30);
            times.push_back(std::move(time_i));
        }

        for (int n = 0; n < N; ++n) {
            double horse_max_dist = horse_dist[n];
            double horse_Speed = horse_speed[n];

            for (int j = 0; j < N; ++j) {
                if(real_dists[n][j] <= horse_max_dist)
                {
                    times[n][j] = real_dists[n][j]/horse_Speed;
                }
            }
            
        }

        //path search for all cases

        //next floyd warshall


        std::vector<std::vector< double >> total_times;

        for (int l1 = 0; l1 < N; ++l1) {
            std::vector<double> t(N, std::numeric_limits<double>::max());
            for (int j = 0; j < N; ++j) {
                t[j] = times[l1][j];
            }
            total_times.push_back(std::move(t));
        }

        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                for (int l = 0; l < N; ++l) {
                    total_times[k][l] = std::min(total_times[k][l], total_times[k][j] + total_times[j][l]);
                }
            }
        }

      /*  for (int j1 = 0; j1 < N; ++j1) {
            for (int j = 0; j < N; ++j) {

                double output = total_times[j1][j] ==  std::numeric_limits<double>::max() ? -1 : total_times[j1][j];

                std::cout << output << " ";
            }
            std::cout << std::endl;
        }*/

        std::cout << "Case #" << i + 1 << ": ";

        std::cout.precision(std::numeric_limits< double >::max_digits10);

        for (int m1 = 0; m1 < Q; ++m1) {
            std::cout << std::fixed << total_times[U[m1]-1][V[m1]-1] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}