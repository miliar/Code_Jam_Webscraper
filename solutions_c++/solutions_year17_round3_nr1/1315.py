#include <bits/stdc++.h>

using namespace std;

//int dirs[4][2]={{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
//int dirs[8][2]={{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

double pi=acos(-1.0);

int main()
{
    //ios::sync_with_stdio(false);
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    //cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:", case_no);
        //cout << "Case #" << case_no << ":";
        cerr << "Start geval " << case_no << endl;
        int N, K;
        scanf("%d %d", &N, &K);
        vector< pair<int, int> > radius_height(N);
        for(int i=0; i<N; i++)
        {
            int tmp1, tmp2;
            scanf("%d %d", &tmp1, &tmp2);
            radius_height[i]=make_pair(tmp1, tmp2);
        }
        sort(radius_height.begin(), radius_height.end());
        double best=0.0;
        for(int bottom=K-1; bottom<N; bottom++)
        {
            double current_surface=0.0;
            current_surface += ((1.0*radius_height[bottom].first)*radius_height[bottom].first)*pi;
            current_surface += (2*pi*radius_height[bottom].first)*radius_height[bottom].second;
            vector<double> others;
            for(int i=0; i<bottom; i++)
            {
                others.push_back((2*pi*radius_height[i].first)*radius_height[i].second);
            }
            sort(others.begin(), others.end());
            reverse(others.begin(), others.end());
            for(int i=0; i<K-1; i++)
            {
                current_surface += others[i];
            }
            best=max(best, current_surface);
        }
        printf(" %.12f\n", best);

    }
    return 0;
}
