
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)

using namespace std;






int main(int argc, char **argv)
{

	unsigned int est[10][2];
       
    freopen("C-test.in", "r", stdin);
    freopen("C-test.out", "w", stdout);

	
    int T; cin >> T;
	unsigned long N; 
	unsigned long K; 

	unsigned int sl, sr;

    getchar();
        
    FOR(ts, 1, T+1){
		
		cin >> N;
		cin >> K;
	
		FOR (i,0,10) { est[i][0]=0; est[i][1]=0; }
			
		est[0][0]=1;
		est[0][1]=N;	
			
		
		//cout << endl << endl << K << ")"; FOR(j,0,10) cout << est[j][0] << '-' << est[j][1] << " "; cout << endl;
		
		while (K>0)
		{
			
			sr = (est[0][1]-1) / 2;	
			if ( (est[0][1]-1)%2 == 0 ) sl=sr; else sl=sr+1;
			
			int lp=0;
			while (est[lp][1] != sl && est[lp][1] != 0) lp++;
			est[lp][1] = sl;
			int rp=0;
			while (est[rp][1] != sr && est[rp][1] != 0) rp++;
			est[rp][1] = sr;
			
			if (K>est[0][0]) {
				
				K -= est[0][0];
				est[lp][0] += est[0][0];
				est[rp][0] += est[0][0];
				
				FOR(j,0,9) {
					est[j][0] = est[j+1][0];
					est[j][1] = est[j+1][1];
				}
			} 
			else {
				K = 0;
			}
			
			 //cout << K << ")"; FOR(j,0,10) cout << est[j][0] << '-' << est[j][1] << " "; cout << endl;
		}	
			
		cout << "Case #" << ts << ": " << sl << " " << sr << endl;
        
    }
  
  
  
    return 0;
}

