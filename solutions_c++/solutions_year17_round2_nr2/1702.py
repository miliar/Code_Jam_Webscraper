#include <bits/stdc++.h>

using namespace std;


int main(){
    freopen("output.out","w",stdout);
    freopen("input.in","r",stdin);
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        int n,r,b,y,temp;
        int m1,m2,m3;
        char m;
        string outp;

        cin >> n >> r >> temp >> y >> temp >> b >> temp;
        vector<pair<int,char> > v(0);
        v.push_back(make_pair(r,'R'));
        v.push_back(make_pair(y,'Y'));
        v.push_back(make_pair(b,'B'));
        sort(v.rbegin(),v.rend());
        if(v[0].first>n/2)
        {
            outp = "IMPOSSIBLE";
        }
        else
        {
            for(int j=0;j<n;j++) outp+='0';
            int pos;
            for(int j=0;j<n;j+=2)
            {
                outp[j]=v[0].second;
                v[0].first--;
                pos=j;
                if(v[0].first==0) break;
            }
            for(int j=pos+1;j<n;j++)
            {
                if(j%2==1) outp[j]=v[1].second,v[1].first--;
                if(j%2==0) outp[j]=v[2].second,v[2].first--;
            }

            for(int j=1;j<pos;j+=2)
            {
                if(v[1].first>0) outp[j]=v[1].second,v[1].first--;
                else if(v[2].first>0) outp[j]=v[2].second,v[2].first--;
            }
        }
        cout << "Case #"<<i+1<<": " << outp<< endl;
    }
    return 0;
}
