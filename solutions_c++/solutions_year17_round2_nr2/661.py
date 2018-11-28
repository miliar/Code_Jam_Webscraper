#include <bits/stdc++.h>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    int n,r,o,y,g,b,v;
    scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
    printf("Case #%d: ",cs);
    int R=v+r+o,Y=o+y+g,B=g+b+v;
    if(r==g&&r+g==n){
      for(int i=0;i<n/2;i++){
	putchar('R');
	putchar('G');
      }
    }
    else if(y==v&&y+v==n){
      for(int i=0;i<n/2;i++){
	putchar('Y');
	putchar('V');
      }
    }
    else if(b==o&&b+o==n){
      for(int i=0;i<n/2;i++){
	putchar('B');
	putchar('O');
      }
    }
    else if((g>0&&r<g+1)||(v>0&&y<v+1)||(o>0&&b<o+1)||R>n/2||B>n/2||Y>n/2){
      printf("IMPOSSIBLE");
    }
    else{
      int C1=(g>0?0:v>0?1:2);
      int C2=(o>0?2:v>0?1:0);
      if(g>0){
	putchar('R');
	r--;
	while(g>0){
	  putchar('G');
	  g--;
	  putchar('R');
	  r--;
	}
	if(v>0&&B>=R&&B>=Y){
	  putchar('B');
	  b--;
	}
      }
      if(v>0){
	putchar('Y');
	y--;
	while(v>0){
	  putchar('V');
	  v--;
	  putchar('Y');
	  y--;
	}
	if(o>0&&R>=B&&R>=Y){
	  putchar('R');
	  r--;
	}
      }
      if(o>0){
	putchar('B');
	b--;
	while(o>0){
	  putchar('O');
	  o--;
	  putchar('B');
	  b--;
	}
      }
      int N=r+b+y;
      if(C1==C2){
	C1=(C1+1)%3;
	C2=(C2+2)%3;
      }
      int c1=(C1==0?r:C1==1?y:b);
      char ch1=(C1==0?'R':C1==1?'Y':'B');
      int c2=(C2==0?r:C2==1?y:b);
      char ch2=(C2==0?'R':C2==1?'Y':'B');
      int c3=N-c1-c2;
      char ch3='R'+'Y'+'B'-ch1-ch2;
      if(c3==N/2){
	if(N%2==0){
	  swap(ch1,ch3);
	  swap(c1,c3);
	}
	else{
	  swap(ch2,ch3);
	  swap(c2,c3);
	}
      }
      if(N%2==0){
	for(int i=0;i<N;i++){
	  if(i%2==0){
	    if(i/2<c1){
	      putchar(ch1);
	    }
	    else{
	      putchar(ch3);
	    }
	  }
	  else{
	    if(i/2<c3-(N/2-c1)){
	      putchar(ch3);
	  }
	    else{
	      putchar(ch2);
	    }
	  }
	}
      }
      else{
	for(int i=0;i<N;i++){
	  if(i%2==0){
	    if(i/2<c1){
	    putchar(ch1);
	    }
	    else{
	      putchar(ch3);
	    }
	  }
	  else{
	    if(i/2<c3-((N+1)/2-c1)){
	      putchar(ch3);
	    }
	    else{
	      putchar(ch2);
	    }
	  }
	}
      }
    }
    putchar('\n');
  }
  return 0;
}
