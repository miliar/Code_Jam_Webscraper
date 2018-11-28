 #include <bits/stdc++.h>
using namespace std;

int n, m, k;

int main()
{
   freopen("r.txt","r",stdin);
   freopen("out.txt","w",stdout);
   cin>>k;
   for(int i=0;i<k;i++){
    cin>>n>>m;
    vector<int>vec, tmp;
    int sz=1, a ,b;
    vec.push_back(n);
    for(int j=0;j<m;j++){
        int pos=0, Max=0;
        for(int u=0;u<sz;u++){
            //printf("%d,",vec[u]);
            if(vec[u]>Max)
               Max=vec[u], pos=u;
        }
        //printf("#%d    ", Max);
        a=b=(Max-1)/2;
        if(Max%2==0)
            b++;
        if(j==m-1)
            break;
        tmp.clear();
        for(int u=0;u<sz;u++){
            if(u==pos)
                tmp.push_back(a), tmp.push_back(b);
            else
                tmp.push_back(vec[u]);
        }
        vec.clear(), sz++;
        for(int u=0;u<sz;u++)
            vec.push_back(tmp[u]);
    }
    cout<<"Case #"<<i+1<<": "<<max(a, b)<<" "<<min(a,b)<<"\n";

   }
    return 0;
}
