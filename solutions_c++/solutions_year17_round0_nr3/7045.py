#include <iostream>
#include <cstdlib>
#include <vector>
#include <string> 
#include <cmath> 

using namespace std; 

// number of intervals after inserting k points in [1..n] 
uint64_t intervals(uint64_t n, uint64_t k){
	return (k<=n)?(k+1):-1; 
}


inline int min(int a,int b){
    return (a<=b)?a:b;
}


inline int max(int a,int b){
    return (a>=b)?a:b;
}
void simulate(uint64_t n, uint64_t k, int caseid)
{
    int winner;
    int left[n+2], right[n+2];
    bool occupied[n+2];
    for(int i = 1; i<=n;i++)
        occupied[i]=false;
    occupied[0] = occupied[n+1] = true;
    for(int i=1; i <= n;i++){
        int counter = i-1;
        while( occupied[counter] == false)
            counter--;
        left[i] = (i-1)-counter;
        counter = i+1;
        while( occupied[counter] == false)
            counter++;
        right[i] = counter-(i+1);
    }
    
    for(int i = 1; i <= k; i++){
        
        vector<int> candidates;
        int criterion_A,criterion_B;
        criterion_A=criterion_B= -RAND_MAX;
        
        // check each position
        for( int pos = 1; pos<=n; pos++){
            if( occupied[pos] == false ){
                if( min(left[pos],right[pos]) == criterion_A )
                    candidates.push_back(pos);
                if( min(left[pos],right[pos]) > criterion_A ){
                    candidates.clear();
                    candidates.push_back(pos);
                    criterion_A = min(left[pos],right[pos]);
                }
            }
        }
        if( candidates.size() == 0 )
        {
            cout<<"Everything is occupied\n";
            return;
        }
        if( candidates.size() == 1 )
            winner = candidates[0];
        
        
        for(int s = 0;  s<candidates.size(); s++){
            int pos = candidates[s];
            //cout<<"Position "<<pos<<"with min(L,R)="<<criterion_A<<" and max(L,R)="<< max(left[pos],right[pos])<<endl;
            if(max(left[pos],right[pos])> criterion_B ){
                winner = pos;
                criterion_B =max(left[pos],right[pos]);
            }
        }
        occupied[winner] = true;
     //   cout<<" Customer "<<  i << " sat at "<< winner <<endl;
        // update all other cells on left and right
        
        for(int ii=1; ii <= n; ii++){
            int counter = ii-1;
            while( occupied[counter] == false)
                counter--;
            left[ii] = (ii-1)-counter;
            counter = ii+1;
            while( occupied[counter] == false)
                counter++;
            right[ii] = counter-(ii+1);
        }
    }
    
    for(int i = 0; i<=n+1; i++){
      //  if(occupied[i]==true)
       //     cout<<"Position "<<i<<" is occupied"<<endl;
    }
   // cout<<left[4]<<" " << right[4] << " " << left[winner]<<" " << right[winner] << " " << endl;
    cout<<"Case #"<<(caseid)<<": "<<max(right[winner], left[winner])<<" "<<min(right[winner], left[winner])<<endl;
}



// length of longest interval after inserting k points in [1..n]
void solve(uint64_t n, uint64_t k, uint64_t* m, uint64_t* M, uint64_t* X)
{
	*m=1;
	*M = 10;
	*X = 10;
}


int main(){
	int T;
	uint64_t n,k;
    uint64_t m,M,X;
    m=M=X=100;
	cin>>T; 
	for(int i=0; i<T; i++){
		cin>>n>>k; 
		solve(n,k,&m,&M,&X);
       // cout<<"Case #"<<(i+1)<<": "<<M<<" "<<m<<endl;
        simulate(n,  k,i+1);
	}
	return 0;
}	 
