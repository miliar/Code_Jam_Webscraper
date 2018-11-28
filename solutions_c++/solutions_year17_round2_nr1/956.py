#include <bits/stdc++.h>

using namespace std;

//int dirs[4][2]={{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
//int dirs[8][2]={{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int main()
{
    //ios::sync_with_stdio(false);
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:", case_no);
        //cout << "Case #" << case_no << ":";
        cerr << "Start geval " << case_no << endl;
        long long D, N;
        scanf("%lld %lld", &D, &N);
        vector< pair<long long, long long> > other_horses(N);
        for(int i=0; i<N; i++)
        {
            long long K, S;
            scanf("%lld %lld", &K, &S);
            other_horses[i]=make_pair(K, S);
        }
        sort(other_horses.begin(), other_horses.end());

        vector< vector< pair<double, double> > > info(N); // <time, km_per_hour>
        info[N-1].push_back(make_pair(1.0*(D-other_horses[N-1].first)/(other_horses[N-1].second), other_horses[N-1].second));
        for(int horse_idx=N-2; horse_idx>=0; horse_idx--)
        {
            double own_pos = other_horses[horse_idx].first;
            double own_speed = other_horses[horse_idx].second;

            int idx=-1;
            double tot_time=0.0;
            double start_pos=other_horses[horse_idx+1].first;
            double crash_time_in_block=-1;
            for(int i=0; i<info[horse_idx+1].size(); i++)
            {
                if(info[horse_idx+1][i].second >= own_speed)
                {
                    tot_time += info[horse_idx+1][i].first;
                    start_pos += info[horse_idx+1][i].first*info[horse_idx+1][i].second;
                }
                else
                {
                    double time_to_crash = (start_pos-own_pos)/(own_speed-info[horse_idx+1][i].second);
                    if(time_to_crash > info[horse_idx+1][i].first)
                    {
                        tot_time += info[horse_idx+1][i].first;
                        start_pos += info[horse_idx+1][i].first*info[horse_idx+1][i].second;
                    }
                    else
                    {
                        tot_time += time_to_crash;
                        crash_time_in_block=time_to_crash;
                        idx=i;
                        break;
                    }
                }
            }
            if(idx==-1)
            {
                info[horse_idx].push_back(make_pair(1.0*(D-own_pos)/own_speed, own_speed));
            }
            else
            {
                info[horse_idx].push_back(make_pair(tot_time, own_speed));
                if(crash_time_in_block != info[horse_idx+1][idx].first)
                {
                    info[horse_idx].push_back(make_pair(info[horse_idx+1][idx].first-crash_time_in_block, info[horse_idx+1][idx].second));
                    for(int i=idx+1; i<info[horse_idx+1].size(); i++)
                    {
                        info[horse_idx].push_back(info[horse_idx+1][i]);
                    }
                }
            }
        }
        double tot_time=0.0;
        for(int i=0; i<info[0].size(); i++)
        {
            tot_time += info[0][i].first;
        }
        double ans = 1.0*D/tot_time;
        printf(" %.12f\n", ans);
    }
    return 0;
}
