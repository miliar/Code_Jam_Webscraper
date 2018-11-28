#include <bits/stdc++.h>

using namespace std;
vector<double> ToBeIncreased;
vector<double> inp;
double DP[100][100];
double solve(int idx,int Left)
{
    if(Left==0)
        return 1.0;
    if(idx==inp.size())
        return 0;
    double &ret=DP[idx][Left];
    if(ret>=0)
        return ret;
    ret=0;
    ret+=(double)inp[idx]*solve(idx+1,Left-1);
    ret+=(double)((double)1-inp[idx])*solve(idx+1,Left);
    return ret;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    int cases=0;
    cin>>T;
    while(T--){
        cases++;
        ToBeIncreased.clear();
        inp.clear();
        for(int i=0;i<100;i++)
            for(int j=0;j<100;j++)
                DP[i][j]=-1;
        int N,K;
        cin>>N>>K;
        double Increment;
        cin>>Increment;
        for(int i=0;i<N;i++){
            double tmp;
            cin>>tmp;
            inp.push_back(tmp);
        }
        sort(inp.begin(),inp.end());
        for(int i=0;i<K;i++){
            ToBeIncreased.push_back(inp.back());
            inp.pop_back();
        }
        reverse(ToBeIncreased.begin(),ToBeIncreased.end());
        for(int i=1;i<ToBeIncreased.size();i++){
            if((double)(ToBeIncreased[i]-ToBeIncreased[0])*i<=Increment){
                Increment-=(double)(ToBeIncreased[i]-ToBeIncreased[0])*i;
                for(int j=0;j<i;j++)
                    ToBeIncreased[j]=ToBeIncreased[i];
            }
            else{
                for(int j=0;j<i;j++){
                    ToBeIncreased[j]+=(double)Increment/(double)i;
                }
                Increment=0;
                break;
            }
        }
        if(Increment!=0){
            for(int i=0;i<ToBeIncreased.size();i++)
                ToBeIncreased[i]+=(double)Increment/ToBeIncreased.size();
        }
        for(int i=0;i<ToBeIncreased.size();i++)
            inp.push_back(ToBeIncreased[i]);
        cout<<"Case #"<<cases<<": "<<fixed<<setprecision(6)<<solve(0,K)<<endl;

    }
    return 0;
}
