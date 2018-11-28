#include<iostream>
using namespace std;
struct cav{
  long long pos, vel;
};
bool compara(cav a, cav b){
  return a.pos<b.pos;
}
cav v[1002];
int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){

    long long D;
    int N;
    cin>>D>>N;

    for(int i=0;i<N;i++)
      cin>>v[i].pos>>v[i].vel;
      /*
    if(t==13){
      cout<<D<<" "<<N<<endl;
      cout<<v[0].pos<<" "<<v[0].vel<<endl;
    }
    */
    sort(v, v+N, compara);
    long double ans;
    if(N==1){
      long double t=(long double)(((long double)D-v[0].pos)/v[0].vel);
      ans = (long double)D/t;
    }else if(N==2){
      if(v[0].vel<=v[1].vel){
        long double t=(long double)(((long double)D-v[0].pos)/v[0].vel);
        ans = (long double)D/t;
      }else{
        long double t = (long double)(v[1].pos-v[0].pos)/(v[0].vel-v[1].vel);
        long double space = (long double)v[0].vel*t;
        space += v[0].pos;
        if(space <= D){
          long double temp = (long double)((long double)D-space)/v[1].vel + t;
          ans = (long double)D/temp;
        }else{
          long double t=(long double)(((long double)D-v[0].pos)/v[0].vel);
          ans = (long double)D/t;
        }

      }
    }
    printf("Case #%d: %Lf\n", t, ans);
  }

}
