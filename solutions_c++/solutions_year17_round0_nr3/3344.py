#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size())
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

bool c (II a,II b) { return ((a.first<b.first) or ((a.first==b.first) and (a.second<b.second))); }

int main(){
    ifstream be("C-large.in");
    ofstream ki("ki");

    int T;
    be>>T;

    for(LL cn=0; cn<T;cn++){
        long long k,n;
        be>>n>>k;
 //       cout<<k<<' '<<n<<'\n';


/*        int a0=((n%2==0)?n:n+1);//paros
        int m0=((n%2==0)?1:0);
        int a1=((n%2==1)?n:n+1);//paratlan
        int m1=((n%2==1)?1:0);*/

        pair<LL,LL> a0=MP(((n%2==0)?n:n+1),((n%2==0)?1:0));
        pair<LL,LL> a1=MP(((n%2==1)?n:n+1),((n%2==1)?1:0));

        long long int akt;
        for(akt=1;akt<k;){
            akt=(akt<<1)+1;
            long long int b0=a1.first/2;
            long long int b1=a0.first-1-b0;

            long long int mm0=2*a1.second+a0.second;
            long long int mm1=a0.second;

            if(b0%2==0){
                a0=MP(b0,mm0);
                a1=MP(b1,mm1);
            }else{
                a1=MP(b0,mm0);
                a0=MP(b1,mm1);
            }
        }
        akt=(akt>>1);


        //cout<<a0.first<<' '<<a0.second<<'\n'<<a1.first<<' '<<a1.second<<'\n';



        long long int kk=k-akt;
        //cout<<k<<'\n';
        if(a0.first<a1.first){
            pair<LL,LL> b=a0;
            a0=a1;
            a1=b;
        }

        long long int tav=((a0.second>=kk)?a0.first:a1.first);
        //cout<<tav<<'\n';

        /*vector<int> L(n+2,0);
        vector<int> R(n+2,0);
        vector<int> a(n+2,0);
        vector<int> b(n+2,0);

        for(int i=1;i<n+1;i++){
            L[i]=i-1;
            R[i]=n-i;
            a[i]=min(L[i],R[i]);
            b[i]=max(L[i],R[i]);
        }
        a[0]=0;a[n+1]=0;b[0]=0;b[n+1]=0;
        int p=0;
        for(int i=0;i<k;i++){
            a[p]=0;b[p]=0;
            int m=0;
            for(int j=n;j>0;j--){
                m=(a[j]>m)?a[j]:m;
            }
            int M=0;

            for(int j=n;j>0;j--){
                if((b[j]>=M)and a[j]==m){M=b[j];p=j;}
            }
            for(int j=p-1;p-j<=L[p];j--){
                R[j]=p-1-j;
                a[j]=min(L[j],R[j]);
                b[j]=max(L[j],R[j]);
            }
            for(int j=p+1;j-p<=R[p];j++){
                L[j]=j-p-1;
                a[j]=min(L[j],R[j]);
                b[j]=max(L[j],R[j]);
            }
        }*/
        //cout<<b[p]<<' '<<a[p]<<'\n';

        ki<<"Case #"<<cn+1<<": "<<tav/2<<' '<<((tav%2==0)?max(tav/2-1,LL(0)):tav/2)<<'\n';
//        cout<<cn+1<<' '<<((b[p]==tav/2) and (a[p]==((tav%2==0)?max(tav/2-1,0):tav/2)))<<'\n';
    }
    be.close();
    ki.close();
	return 0;
}
