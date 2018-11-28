#include <cstdlib>
#include <iostream>

using namespace std;
char map_x[200][200];
char map_p[200][200];
char newmap_x[200][200];
char newmap_p[200][200];
int row_occu_x[200];
int col_occu_x[200];
int row_occu_p[800];
int col_occu_p[800];


void init_map(int n){
   for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	     map_x[i][j]='.';
		 map_p[i][j]='.';
	  }
	  row_occu_x[i]=0;
	  col_occu_x[i]=0;
	  row_occu_p[i]=0;
	  col_occu_p[i]=0;
   }
   for(int i=0;i<4*n;i++){
      row_occu_p[i] = 0;
      col_occu_p[i] = 0;
   }
}

void copy_map(int n){
   for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	     newmap_x[i][j] = map_x[i][j];
	     newmap_p[i][j] = map_p[i][j];
	  }
   }
}

int main(){
   int T;
   cin >> T;
   
   for(int t=1;t<=T;t++){
      int N, M;
      cin >> N >> M;
      init_map(N);
      for(int m=1; m<=M;m++){
	     char c;
	     int x, y;
	     cin >> c >> x >> y;
	     bool got_x=false, got_p=false; 
	     if(c=='x') got_x = true;
	     else if(c=='+') got_p = true;
	     else if(c=='o') {
		    got_x=got_p=true;
		 }
	     
		 if(got_x) {
		    map_x[x-1][y-1] = 'x';
		    
		    row_occu_x[x-1] = 1;
		    col_occu_x[y-1] = 1;
		 }
		 if(got_p) {
		    map_p[x-1][y-1] = '+';
		    
		    row_occu_p[(x-1)+(y-1)+N] = 1;
		    col_occu_p[(x-1)-(y-1)+N] = 1;
		 }
	  }
	  copy_map(N);
	  
	  // handle "x"
	  for(int i=0;i<N;i++){
		    for(int j=0;j<N;j++){
			   if(row_occu_x[i]==0 && col_occu_x[j]==0) {
			      newmap_x[i][j] = 'x';
			      row_occu_x[i]=1;
			      col_occu_x[j]=1;
			   }
			}
	   }
	   
	   /*	 
	   // handle "+"
	   // 1. skip those on two diags
	   for(int i=0;i<N;i++){
		    for(int j=0;j<N;j++){
		       if(i+j==N-1 || i-j==0)
			      continue; 
			   if(row_occu_p[i+j+N]==0 && col_occu_p[i-j+N]==0) {
			      newmap_p[i][j] = '+';
			      row_occu_p[i+j+N] = 1;
			      col_occu_p[i-j+N] = 1;
			   }
			}
	    }
	    // 2. diags
	    if(row_occu_p[N-1+N]==0){
		   newmap_p[N-1][0] = '+';
		   row_occu_p[N-1+0+N] = 1;
		   col_occu_p[N-1-0+N] = 1;
		}
		if(col_occu_p[0+N]==0){
		   newmap_p[0][0] = '+';
		   row_occu_p[0+0+N] = 1;
		   col_occu_p[0-0+N] = 1;
		}
		*/
		// handle "+" : small 
		for(int i=0;i<N;i++){
			if(i!=0 && i!=N-1)
			   continue;
		    for(int j=0;j<N;j++){
		       if(row_occu_p[i+j+N]==0 && col_occu_p[i-j+N]==0) {
			      newmap_p[i][j] = '+';
			      row_occu_p[i+j+N] = 1;
			      col_occu_p[i-j+N] = 1;
			   }
			}
	    }
		
	    int count=0;
	  char out_char[100000];
	  int out_posx[100000];
	  int out_posy[100000]; 
	  
	  for(int i=0;i<N;i++){
	     for(int j=0;j<N;j++){
		    if(map_x[i][j]==newmap_x[i][j] && map_p[i][j]==newmap_p[i][j])
		       continue;
		    if(map_x[i][j]==newmap_x[i][j] && map_p[i][j]!=newmap_p[i][j]){
		       
			   if(map_x[i][j] == '.')  out_char[count] = '+';
			   else if(map_x[i][j] == 'x') out_char[count] = 'o';
			   out_posx[count]=i+1;
			   out_posy[count]=j+1;
			   count++;
			}
			else if(map_x[i][j]!=newmap_x[i][j] && map_p[i][j]==newmap_p[i][j]){
			   
			   if(map_p[i][j]=='.')  out_char[count]='x';
			   else if(map_p[i][j]=='+') out_char[count]='o';
			   out_posx[count]=i+1;
			   out_posy[count]=j+1;
			   count++; 
			}
			else{
			   
			   out_char[count]='o';
			   out_posx[count]=i+1;
			   out_posy[count]=j+1;
			   count++;
			}
		 }
	  }
	  
	  int total = 0;
	  for(int i=0;i<N;i++){
	     for(int j=0;j<N;j++){
		    if(newmap_x[i][j] == 'x') total++;
		    if(newmap_p[i][j] == '+') total++;
		 }
	  }
	  
	  // output to file
	  cout << "Case #" << t << ": " << total << " " << count << endl;
	  for(int c=0;c<count;c++){
	     cout << out_char[c] << " " << out_posx[c] << " " << out_posy[c] << endl;
	  }
	  
	  
	  
	  
   }
}
