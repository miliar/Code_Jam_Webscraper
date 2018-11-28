#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
#define int unsigned long long int

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;



int N;
 main() {
     //                char take='l';
                    char take='s';
  if (take=='s') {
        freopen("small3.in","rt",stdin);
        freopen("small.out","wt",stdout);
   } else if (take=='l') {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
	    cout<<"error";
    }
    cin>>N;
    rep2(nn,1,N+1) {
        printf("Case #%d: ", nn);
        int n;
        cin>>n;
        int k;
        cin>>k;
        int *stl=new int[n+2],*maxdif=new int[n+2];

        int *ls=new int[n+2],*rs=new int[n+2];
        rep(i,n+2){stl[i]=ls[i]=rs[i]=maxdif[i]=0;}
        int maxpos=0;

        stl[0]=stl[n+1]=1;

        while(k--){
                   // cout<<endl;                    rep(i,n+2)                    cout<<stl[i]<<" ";                    cout<<endl;

                    rep(i,n+2){ls[i]=rs[i]=0;}
                    int mval=0;
                    for(int i=0;i<n+2;i++)
                        {
                            for( int j=i;j>0&&stl[j]!=1;j--)
                            ls[i]++;

                            for(int j=i;j<n+2&&stl[j]!=1;j++)
                            rs[i]++;
                            maxdif[i]=min(ls[i],rs[i]);
                            if(mval<=  maxdif[i]){
                                mval=  maxdif[i];
                        }
                        }



                    int tm1=0 ;

                    rep(i,n+2){
                       //        cout<<endl<<"i=  "<<i<<"  ls="<<ls[i]<<"  rs="<<rs[i]<<"  min  "<<maxdif[i];
                                if(mval==maxdif[i]&&tm1<= max(ls[i],rs[i])){
                                                                 tm1=max(ls[i],rs[i]);
                                                                 maxpos=i;
                                                                }

                                }
                //  cout<<"   maxpos=  "<<maxpos;

                    stl[maxpos]=1;


                }

       cout<<ls[maxpos]-1<<' '<<rs[maxpos]-1<<endl;
        }


    return 0;
}
