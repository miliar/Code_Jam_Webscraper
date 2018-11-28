#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void work(int n,int k);

int main()
{
    int T,n,k;
    cin >> T;
    for(int i = 1;i <= T;++i)
    {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        work(n,k);
    }
}

void work(int n,int k)
{
    vector<int> room;
    room.push_back(0);
    room.push_back(n + 1);
    int ls,rs;
    for(int i = 0;i < k;++i)
    {
        int Max=0,r,pos;
        for(int j = 0;j < room.size() - 1;++j)
        {
            int d = room[j + 1] - room[j];
            if(d > Max)
            {
                Max = d;
                r = room[j] + (d >> 1);
                pos = j + 1;
            }
        }
        room.insert(room.begin() + pos,r);
        if(i == k - 1)
        {
            //cout << pos << endl;
            ls = room[pos] - room[pos - 1];
            rs = room[pos + 1] - room[pos];
        }
    }
    cout << max(ls,rs) - 1 << " " << min(ls,rs) - 1 << endl;
    /*for(auto it:room)
        cout << it << " ";
    cout << endl;*/
}
