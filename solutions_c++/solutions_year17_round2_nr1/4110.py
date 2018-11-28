#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;
    fin >> T;

    for (int t = 0; t < T; t++)
    {
        double result;

        int D;
        int N;

        fin >> D >> N;

        vector<pair<int,double>> horses;
        for (auto i = 0; i < N; i++)
        {
            int pos;
            int speed;
            fin >> pos >> speed;
            horses.push_back({pos, speed});
        }

        double maxTime = -1;

        for (int i = 0; i < N; i++)
        {
            // pos + speed * t = D, t = D - pos/speed

            double minIntersect = (D - horses[i].first) / horses[i].second;
            double minSpeed = horses[i].second;

            if (maxTime == -1)
            {
                maxTime = minIntersect;
            }

            for (int r = i + 1; r < N; r++)
            {
                if (horses[r].second == horses[i].second)
                    continue;
                double intersect = (horses[i].first - horses[r].first) / (horses[r].second - horses[i].second);
                if (intersect < minIntersect)
                {
                    double pos = horses[i].first + horses[i].second * intersect;
                    double speed = min(horses[i].second, horses[r].second);
                    double time = (D - pos) / speed + intersect;
                    if (time > maxTime)
                    {
                        maxTime = time;
                    }
                }
            }
        }

        result = D / maxTime;

        double minIntersect = D / result;

        for (int i = 0; i < N; i++)
        {
            double intersect = (horses[i].first - 0) / (result - horses[i].second);
            if (intersect < minIntersect)
            {
                double pos = horses[i].first + horses[i].second * intersect;
                double speed = min((double)horses[i].second, result);
                double time = (D - pos) / speed + intersect;
                double finalSpeed = D / time;
                if (finalSpeed == numeric_limits<double>::min())
                {
                    break;
                }
                if (finalSpeed < result)
                {
                    result = finalSpeed;
                }
            }
        }

        fout.precision(10);
        fout.setf( std::ios::fixed, std:: ios::floatfield );
        fout << "Case #" << (t+1) << ": " << result << endl;
    }

    return 0;
}