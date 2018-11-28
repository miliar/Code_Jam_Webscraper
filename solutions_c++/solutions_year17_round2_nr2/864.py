#include <bits/stdc++.h>

using namespace std;

//int dirs[4][2]={{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
//int dirs[8][2]={{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

string word="ROYGBV";
char get_char(int idx)
{
    return word[idx];
}

void impossible()
{
    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    //scanf("%d", &tc);
    cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        //printf("Case #%d: ", case_no);
        cout << "Case #" << case_no << ": ";
        cerr << "Start geval " << case_no << endl;
        int N;
        cin >> N;
        vector< pair<int, char> > v(6);
        for(int i=0; i<6; i++)
        {
            int tmp;
            cin >> tmp;
            char ch = get_char(i);
            v[i]=make_pair(tmp, ch);
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        if(v[1].first+v[2].first<v[0].first)
        {
            impossible();
            continue;
        }
        vector<string> ans;
        for(int i=0; i<v[1].first; i++)
        {
            string s="";
            s += v[0].second;
            s += v[1].second;
            ans.push_back(s);
        }
        for(int i=0; i<v[0].first-v[1].first; i++)
        {
            string s = "";
            s += v[0].second;
            s += v[2].second;
            ans.push_back(s);
        }
        v[2].first -= v[0].first-v[1].first;
        for(int i=0; i<ans.size(); i++)
        {
            cout << ans[i];
            if(v[2].first>0)
            {
                v[2].first--;
                cout << v[2].second;
            }
        }
        cout << endl;
    }
    return 0;
}
