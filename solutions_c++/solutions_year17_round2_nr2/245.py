#include <iostream>
#include <vector>
#include <limits>
#include <iomanip>

int main() {
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {

        int N, R, O, Y, G, B, V;
        std::cin >> N >> R >> O >> Y >> G >> B >> V;
        std::vector<int> vec(3);


        bool solution_found = false;
        bool strange_case = false;

        if((R == G and R > 0 and R + G < N) or (Y == V and Y > 0 and Y + V < N) or (B == O and B > 0 and B + O < N))
        {
            std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
            continue;
        }

        int orN = N;
        int orR = R;
        int orY = Y;
        int orB = B;

        R -= G;
        Y -= V;
        B -= O;

        if(R < 0 or Y < 0 or B < 0)
        {
            std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
            continue;
        }

        N = R + Y + B;
        std::vector<int> sol(N, -1);


        //std::cout << "R: " << R << " Y: " << Y << " B: " << B << std::endl;

        for (int k = 0; k < 3; ++k) {
            vec[0] = R;
            vec[1] = Y;
            vec[2] = B;

            std::fill(sol.begin(), sol.end(), -1);

            if(N == 0)
            {
                if(R == 0 and Y == 0 and B== 0)
                {
                    int help;
                    if(orR > 0)
                    {
                        help = 0;
                    }
                    if(orY > 0)
                    {
                        help = 1;
                    }
                    if(orB > 0)
                    {
                        help = 2;
                    }

                    sol.resize(orN);
                    for (int j = 0; j < sol.size()/2; ++j) {
                        sol[2*j] = help;
                        sol[2*j+1] = help+3;
                    }
                    solution_found = true;
                    strange_case = true;
                    break;
                }
            }

                if(vec[k] <= 0)
            {
                continue;
            }


            sol[0] = k;
            vec[k]--;

            for (int j = 1; j < N; ++j) {

                if(sol[j-1] == 0)
                {
                    if(vec[1] <= vec[2] and vec[2] > 0)
                    {
                        sol[j] = 2;
                        vec[2]--;
                    }
                    else
                    {
                        if(vec[1] == 0)
                        {
                            break;
                        }
                        sol[j] = 1;
                        vec[1]--;
                    }

                }

                if(sol[j-1] == 1)
                {
                    if(vec[0] <= vec[2] and vec[2] > 0)
                    {
                        sol[j] = 2;
                        vec[2]--;
                    }
                    else
                    {
                        if(vec[0] == 0)
                        {
                            break;
                        }
                        sol[j] = 0;
                        vec[0]--;
                    }

                }

                if(sol[j-1] == 2)
                {
                    if(vec[1] <= vec[0] and vec[0] > 0)
                    {
                        sol[j] = 0;
                        vec[0]--;
                    }
                    else
                    {
                        if(vec[1] == 0)
                        {
                            break;
                        }
                        sol[j] = 1;
                        vec[1]--;
                    }

                }

            }

          /*  for (int l = 0; l < sol.size(); ++l) {
                std::cout << sol[l];
            }

            std::cout << std::endl;*/


            if(sol.back() != -1 and sol.back() != sol[0])
            {
                solution_found = true;
                break;
            }
        }

        std::string S;
        
        if(solution_found)
        {
            bool found_R = strange_case;
            bool found_Y = strange_case;
            bool found_B = strange_case;

            for (int j = 0; j < sol.size(); ++j) {
                if(sol[j] == 0)
                {
                    S.push_back('R');
                    if(not found_R)
                    {
                        for (int k = 0; k < G; ++k) {
                            S.push_back('G');
                            S.push_back('R');
                        }
                        found_R = true;
                    }
                }
                if(sol[j] == 1)
                {
                    S.push_back('Y');
                    if(not found_Y)
                    {
                        for (int k = 0; k < V; ++k) {
                            S.push_back('V');
                            S.push_back('Y');
                        }
                        found_Y = true;
                    }
                }
                if(sol[j] == 2)
                {
                    S.push_back('B');
                    if(not found_B)
                    {
                        for (int k = 0; k < O; ++k) {
                            S.push_back('O');
                            S.push_back('B');
                        }
                        found_B = true;
                    }
                }
                if(sol[j] == 3)
                {
                    S.push_back('G');
                }
                if(sol[j] == 4)
                {
                    S.push_back('V');
                }
                if(sol[j] == 5)
                {
                    S.push_back('O');
                }
            }

        }
        else
        {
            S = "IMPOSSIBLE";
        }

        std::cout << "Case #" << i + 1 << ": " << S << "\n";
    }
    return 0;
}