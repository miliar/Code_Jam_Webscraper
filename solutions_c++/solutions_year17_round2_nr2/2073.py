//#define CHECKING

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

int T, N, R, O, Y, G, B, V, Rr, Yr, Br;
string result;
const char Op[]="OB", Gp[]="GR", Vp[]="VY";

int main()
{
#ifndef CHECKING
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#endif
   scanf("%d",&T);
   for(int i=0;i<T;i++) {
	   scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
	   Br=B-O;
	   Rr=R-G;
	   Yr=Y-V;
	   if(Br<=Rr+Yr && Rr<=Br+Yr && Yr<=Br+Rr) {
		   result.resize(0);
		   if(Br) {
			   result+='B';
			   for(;O;O--) result+=Op;
			   Br--;
		   }
		   for(;Br;Br--) {
			   if(Rr>Yr) {
				   result+='R';
				   for(;G;G--) result+=Gp;
				   Rr--;
			   }
			   else if(Rr==0 && Yr==0) {
				   if(G) for(;G;G--) result+=Gp;
				   else for(;V;V--) result+=Vp;
			   }
			   else if(Rr<=Yr) {
				   result+='Y';
				   for(;V;V--) result+=Vp;
				   Yr--;
			   }
			   result+='B';
		   }
		   for(;Rr||Yr||G||V;) {
			   if(Rr<Yr) {
				   result+='Y';
				   for(;V;V--) result+=Vp;
				   Yr--;
			   }
			   else if(Rr==0 && Yr==0) {
				   if(G) for(;G;G--) result+=Gp;
				   else for(;V;V--) result+=Vp;
			   }
			   else if(Rr>Yr) {
				   result+='R';
				   for(;G;G--) result+=Gp;
				   Rr--;
			   }
			   else if(Rr==Yr) {
				   if(result.size()==0 || result[result.size()-1]=='R') {
					   result+='Y';
					   for(;V;V--) result+=Vp;
					   Yr--;
				   }
				   else {
					   result+='R';
					   for(;G;G--) result+=Gp;
					   Rr--;
				   }
			   }
			   
		   }
	   }
	   else
		   result="IMPOSSIBLE";
	   printf("Case #%d: %s\n",i+1,result.c_str());
   }
#ifdef CHECKING
   system("PAUSE");
#endif
   return 0;
}