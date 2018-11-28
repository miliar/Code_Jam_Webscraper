#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1010;

struct Node{
   int pos, vel;
   Node() {};
   Node(int pos_, int vel_): pos(pos_), vel(vel_) {};
   bool operator < (const Node& other) const{
      return pos < other.pos;
   }
};

int tc, D, N;
Node a[MAX_N];
long double ans;

long double intersection(Node x, Node y){
   if( x.vel <= y.vel ) return D;
   return min(1.0 * D, 1.0 * ( y.pos * x.vel - x.pos * y.vel ) / (x.vel - y.vel) );
}

void solve(int t){
   sort(a, a + N);
   if( N == 1 ){
      int d = D - a[0].pos;
      long double t = 1.0 * d / a[0].vel;
      ans = 1.0 * D / t;
   }
   if( N == 2 ){
      long double pos = intersection(a[0], a[1]), t;
      t = max( 1.0 * ( pos - a[0].pos ) / a[0].vel, 1.0 * ( pos - a[1].pos ) / a[1].vel );
      if( fabs(D - pos) > 1e-9 )
         t += 1.0 * ( D - pos ) / ( min(a[0].vel, a[1].vel) );
      ans = 1.0 * D / t;
   }
   printf("Case #%d: %.12Lf\n", t, ans);
}

void read(){
   scanf("%d %d", &D, &N);
   for(int i = 0; i < N; i++)
      scanf("%d %d", &a[i].pos, &a[i].vel);
}

int main(){
   scanf("%d", &tc);
   for(int t = 1; t <= tc; t++){
      read();
      solve(t);
   }
   return(0);
}
