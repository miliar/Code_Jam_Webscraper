#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

struct horse
{
    double pos;
    double speed;
};

bool Compare(horse a,horse b);

int main()
{
    int T;
    cin >> T;
    
    for(int t = 0; t < T; t++)
    {
        long double D, N;
        cin >> D;
        cin >> N;
        vector<horse> horses;
        for(int i = 0; i < N; i++)
        {
            horse temp;
            double p, v;
            cin >> p;
            cin >> v;
            temp.pos = p;
            temp.speed = v;
            horses.push_back(temp);
        }
        sort(horses.begin(),horses.end(),Compare);

        double vel = 0.0;

        double first = horses[0].speed;
        double max_time = 0.0;
        int slowest = -1;
        for(int i = 0; i < horses.size(); i++)
        {
            for(int j = i+1; j < horses.size(); j++)
            {
                double time = (horses[i].pos - horses[j].pos)/(horses[j].speed - horses[i].speed);
                if(time < 0 || (horses[i].pos+horses[i].speed*time > D))
                    continue;
                else
                {
                    int id;
                    double smaller = min(horses[i].speed,horses[j].speed);
                    if(smaller == horses[i].speed)
                        id = i;
                    else
                        id = j;
                    if((D-horses[id].pos)/smaller > max_time)
                    {
                        max_time = (D-horses[id].pos)/smaller;
                        slowest = id;
                    }
                }
            }            
        }
        if(max_time == 0)
            vel = double(D)/((D-horses[0].pos)/(horses[0].speed));
        else
            vel = double(D)/((D-horses[slowest].pos)/(horses[slowest].speed));
        cout<<fixed<< "Case #"<<t+1<<": "<<vel<< endl;
    } 
    return 0;
}
bool Compare(horse a,horse b)
{
    return a.pos<b.pos;
}
