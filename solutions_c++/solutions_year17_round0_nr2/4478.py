
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)

using namespace std;

	

int main(int argc, char **argv)
{
       
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small0.out", "w", stdout);

	char xi[20];
	
    int T; cin >> T;
    getchar();
        
    FOR(ts, 1, T+1){
		
	
		int nx=0;	
		
		do{
			xi[nx] = getchar();
			nx++;
		}while (xi[nx-1]>='0' && xi[nx-1]<='9');
		nx--;
		
		
		if (nx==1) cout << "Case #" << ts << ": " << xi[0] << endl;
		else{

			int i=0;
			while ( (xi[i] <= xi[i+1]) && (i < (nx-1)) ) i++;
		
			
			//if (xi[i] > xi[i+1])  {
			if (i<(nx-1))  {
				
				char xb = xi[i];
				
				int j=0;
				while (xi[j]!=xb) j++;
				
				xi[j] = xi[j]-1; 
				j++;
				
				while (j<nx) {
					
					xi[j] = '9';
					j++;
				}
				
				
				
				
			}
			
			cout << "Case #" << ts << ": ";
			
			i=0;
			while (xi[i]=='0') { i++; }
			while (i<nx) { cout << xi[i]; i++; }
			cout << endl;

		}
	 
        
    }
  
  
  
    return 0;
}

