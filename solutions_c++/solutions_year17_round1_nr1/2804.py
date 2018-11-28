#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int Test;
	cin>>Test;
	for(int q=1;q<=Test;q++){
	    cout<<"Case #"<<q<<":\n";
	    int R,C;
	    cin>>R>>C;
	    char arr[R][C];
	    for(int  i=0;i<R;i++){
	        for(int j=0;j<C;j++){
	            cin>>arr[i][j];      
	        }
	    }
	    for(int  i=0;i<R;i++){
	        for(int j=0;j<C;j++){
	            int k=i+1;
	            if(arr[i][j]!='?'){
	            while(k<R && arr[k][j]=='?') arr[k++][j]=arr[i][j];
	            k=i-1;
	            while(k>=0 && arr[k][j]=='?') arr[k--][j]=arr[i][j];
	            }
	        }
	    }
	   // col checking
	       int p=0;
	        while(p<C && arr[0][p]=='?') p++;
	       p=p-1;
	   if(p>=0)
	    for(int  i=p;i>=0;i--){
	        for(int j=0;j<R;j++){
	            arr[j][i]=arr[j][i+1];
	        }
	        
	    }
	        p=C-1;
	        while(p>=0 && arr[0][p]=='?') p--;
            p=p+1;
            
            if(p<C)
            for(int i=p;i<C;i++){
	        for(int j=0;j<R;j++){
	            arr[j][i]=arr[j][i-1];
	        }
	        }
	    
	    for(int  i=0;i<R;i++){
	        for(int j=0;j<C;j++){
	            if(arr[i][j]=='?'){
	                    arr[i][j]=arr[i][j+1];
	            }
	        }
	    }
	  
	    
	    for(int  i=0;i<R;i++){
	        for(int j=0;j<C;j++){
	        cout<<arr[i][j];
	        }
	        	        cout<<"\n";
	    }
	   
	    
	}
	return 0;
}

