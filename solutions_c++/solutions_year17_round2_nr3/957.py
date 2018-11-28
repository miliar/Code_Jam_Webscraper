#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int test = 1;test<=t;test++)
    {
        int N,Q;
        cin >> N >> Q;
        long long E[N];
        long long S[N];
        for(int i = 0;i<N;i++)
        {
            cin >> E[i] >> S[i];
        }
        long long map[N][N];
        for(int from = 0;from<N;from++)
        {
            for(int to = 0;to<N;to++)
            {
                cin >> map[from][to];
            }
        }

        cout << "Case #" << test << ": ";
        for(int q = 0;q<Q;q++)
        {
            int start,end;
            cin >> start >> end;
            start--;
            end--;

            double minarrive[N];
            bool fixed[N];
            for(int i = 0;i<N;i++)
            {
                minarrive[i] = 1000000000000000;
                fixed[i] = false;
            }

            //set start conditions
            minarrive[start] = 0;
            while(fixed[end] == false)
            {
                //find smallest arrive at fixed
                double minarr = 10000000000000000;
                int current_city = 0;
                for(int i = 0;i<N;i++)
                {
                    if(fixed[i] == false and minarrive[i] < minarr)
                    {
                        current_city = i;
                        minarr = minarrive[i];
                    }
                }

                //set current city to fixed and get on that horse
                if(fixed[current_city])
                {
                    break;
                }

                fixed[current_city] = true;
                long long dis_from_curr[N];
                bool dis_fixed[N];
                for(int i = 0;i<N;i++)
                {
                    dis_from_curr[i] = 1000000000000000;
                    dis_fixed[i] = false;
                }
                dis_from_curr[current_city] = 0;
                for(int dis_i = 0;dis_i<N;dis_i++)
                {
                    //find smallest distance not fixed
                    long long mindis = 10000000000000000;
                    int dis_city = 0;
                    for(int i = 0;i<N;i++)
                    {
                        if(dis_fixed[i] == false and dis_from_curr[i] < mindis)
                        {
                            mindis = dis_from_curr[i];
                            dis_city = i;
                        }
                    }

                    if(dis_fixed[dis_city] == true)
                    {
                        break;
                    }

                    dis_fixed[dis_city] = true;
                    for(int dis_to = 0;dis_to < N;dis_to++)
                    {
                        if(map[dis_city][dis_to] != -1)
                        {
                            dis_from_curr[dis_to] = min(dis_from_curr[dis_to],map[dis_city][dis_to] + mindis);
                        }
                    }
                }

                /*
                cout << "Distances from city:" << current_city << endl;
                for(int i = 0;i<N;i++)
                {
                    cout << dis_from_curr[i] << endl;
                }
                cout << endl;*/

                for(int i = 0;i<N;i++)
                {
                    if(dis_from_curr[i] <= E[current_city])
                    {
                        minarrive[i] = min(minarrive[i],minarr + ((dis_from_curr[i]+0.0) / S[current_city]));
                    }
                }

                /*cout << "Minarrive matrix outputs" << endl;
                for(int i = 0;i<N;i++)
                {
                    cout << minarrive[i] << endl;
                }*/

            }
            cout << setprecision(15) << minarrive[end] << " ";
        }
        cout << endl;

    }
}
