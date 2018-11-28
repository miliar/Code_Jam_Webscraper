#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <fstream>
#include <map>
using namespace std;

int T;

int main()
{
//    ifstream fin("C-large.in");
//    ofstream fout("Answer.out");
//    cin.rdbuf(fin.rdbuf());
//    cout.rdbuf(fout.rdbuf());
    cin>>T;
    for (int cases=1; cases<=T; cases++)
    {
        map<long long,long long,greater<long long>> M;
        long long N,K,Cnt=0;
        long long AnsMax=0,AnsMin=0;
        cin>>N>>K;
        M.insert({N,1});
        while (Cnt<K)
        {
            auto it=M.begin();
            long long n=(*it).first;
            long long t=(*it).second;

            long long a=(n+1)/2-1,b=n-a-1;
            if (n==1) a=b=0;

            //cout<<Cnt<<" "<<n<<" "<<t<<"          "<<a<<" "<<b<<endl;

            Cnt+=t;
            if (Cnt>=K)
                AnsMax=max(a,b),AnsMin=min(a,b);

            if (a==b)
                M[a]+=t*2;
            else
                M[a]+=t,M[b]+=t;
            M.erase(it);
        }
        cout<<"Case #"<<cases<<": "<<AnsMax<<" "<<AnsMin<<endl;
    }
    return 0;
}
