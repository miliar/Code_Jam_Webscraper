/*-------property of the half blood prince-----*/

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>
#define MIN(X,Y) X<Y?X:Y
#define MAX(X,Y) X>Y?X:Y
#define ISNUM(a) ('0'<=(a) && (a)<='9')
#define ISCAP(a) ('A'<=(a) && (a)<='Z')
#define ISSML(a) ('a'<=(a) && (a)<='z')
#define ISALP(a) (ISCAP(a) || ISSML(a))
#define MXX 10000000000
#define MNN -MXX
#define ISVALID(X,Y,N,M) ((X)>=1 && (X)<=(N) && (Y)>=1 && (Y)<=(M))
#define LLI long long int
#define VI vector<int>
#define VLLI vector<long long int>
#define MII map<int,int>
#define SI set<int>
#define PB push_back
#define MSI map<string,int>
#define PII pair<int,int>
#define PLLI pair<LLI,LLI>
#define FREP(i,I,N) for(int (i)=(I);(i)<=(N);(i)++)
#define eps 0.0000000001
#define RFREP(i,N,I) for(int (i)=(N);(i)>=(I);(i)--)
#define SORTV(VEC) sort(VEC.begin(),VEC.end())
#define SORTVCMP(VEC,cmp) sort(VEC.begin(),VEC.end(),cmp)
#define REVV(VEC) reverse(VEC.begin(),VEC.end())
#define MDD 1000000007
using namespace std;
using namespace __gnu_pbds;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction


typedef tree < int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update > ordered_set;

ifstream fin("in.txt");
ofstream fout("out.txt");

LLI sttonum(string oka){
    LLI s=0;
    int l=oka.size();
    FREP(i,0,(l-1)){
        s=s*10+oka[i]-'0';
    }
    return s;
}

int main(){
    int t;
    fin>>t;
    int cs=1;
    while(t--){
        set<PII>dhishum;
        LLI n,cnt;
        fin>>n>>cnt;
        int idx=1;
        dhishum.insert(make_pair(-n,idx));
        set<PII>::iterator it;
        int person=1;
        int mxans,mnans;
        while(true){
            it=dhishum.begin();
            PII val=*it;
            dhishum.erase(val);
            int ghor=-(val.first);
            ghor--;
            //fout<<ghor<<"\n";
            if(ghor%2==0){
                mxans=ghor/2;
                mnans=ghor/2;
            }
            else{
                mxans=ghor/2+1;
                mnans=ghor/2;
            }
            if(person==cnt){
                break;
            }
            if(mxans==0 && mnans==0)break;
            person++;
            dhishum.insert(make_pair(-mxans,++idx));
            dhishum.insert(make_pair(-mnans,++idx));
        }
        cout<<"Case #"<<cs++<<": "<<mxans<<" "<<mnans<<"\n";
    }
    return 0;
}
