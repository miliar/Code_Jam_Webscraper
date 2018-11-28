#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#define FOR(i,a,b) for(int i=a;i<b;i++)
using namespace std;
typedef long long ll;
int main(){
  freopen("input1.txt","r",stdin);
  freopen("output1.txt","w",stdout);
  int tt;
  cin>>tt;
  FOR(ttnum,1,tt+1){
    ll d,n;
    cin>>d>>n;
    double max_time = 0.0;
    FOR(i,0,n){
      ll ki,si1;
      cin>>ki>>si1;
      double curr_time = ((double)(d-ki))/((double)(si1));
      if(curr_time>max_time){
	max_time = curr_time;
      }
    }
    double result = (((double)(d))/max_time);
    cout<<"Case #"<<ttnum<<": "<<fixed<<setprecision(6)<<result<<endl;
  }
  return 0;
}
