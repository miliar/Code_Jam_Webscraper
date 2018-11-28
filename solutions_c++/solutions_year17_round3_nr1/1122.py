#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iomanip>
#define _USE_MATH_DEFINES

struct Cake{
   double r; 
   double h;
   int id;
};

struct CompCakeRH {
   bool operator() (Cake a, Cake b) {
      return a.r*a.h < b.r*b.h;
   }
} compCakeRH;

struct CompCakeR {
   bool operator() (Cake a, Cake b) {
      return (a.r < b.r) || (a.r==b.r && a.h < b.h);
   }
} compCakeR;

using namespace std;

int main(){
   int T;
   int K, N;
   cin >> T;
   Cake* cake = new Cake[2000];
   Cake* cake_ori = new Cake[2000];
   for(int t=1;t<=T;t++){
      cin >> N >> K;
      for(int i=0;i<N;i++){
	     cin >> cake[i].r >> cake[i].h;
	     cake[i].id = i;
	     cake_ori[i].r = cake[i].r;
	     cake_ori[i].h = cake[i].h;
	     cake_ori[i].id = cake[i].id;
	  }
	  sort(cake, cake+N, compCakeR);
	  
	  
	  
	  
	  double maxArea = 0;
	  for(int i=K-1;i<N;i++){
	  	 sort(cake, cake+i+1, compCakeR);
	     double area = M_PI*cake[i].r*cake[i].r;
	     int id_maxR = cake[i].id;
	     sort(cake, cake+i+1, compCakeRH);
	     bool met = false;
	     for(int j=i; j>=i-K+2;j--){
		    area += 2*M_PI*cake[j].r*cake[j].h;
		    if(cake[j].id == id_maxR) met = true;
		 }
		 if(met) 
		    area += 2*M_PI*cake[i-K+1].r*cake[i-K+1].h;
		 else
		    area += 2*M_PI*cake_ori[id_maxR].r*cake_ori[id_maxR].h;
		 
		 if(area > maxArea) maxArea = area;
	  }
	  cout << "Case #" << t << ": " << fixed << setprecision(6) << maxArea << endl; 
   }


} 
