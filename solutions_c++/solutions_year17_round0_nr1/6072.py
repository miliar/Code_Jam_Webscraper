#include<iostream>
#include<string>

using namespace std;

int string_count(string s,int k){
    int cnt=0,i,j,len,l;
    len=s.length();
	for(i=0;i<=len-k;i++){
        if(s[i]=='-'){
    	    j=k;  l=i;  
	   	    while(j--)
	   	    {
	            if(s[l]=='-')
	                s[l]='+';
		        else
			        s[l]='-';
			    l++;
	        }
		    cnt++;
        }
    }
    j=len-1;
	while(j>len-k-1){
        if(s[j]=='-')
        {
	        cnt=-1;
            break;
        }
        j--;
    }
    return cnt;
}

int main(){
   int test,l,i,j;
   cin >> test;
   for(int l=1;l<=test;l++){
      	string s;
	    int k,len,flag;
    	cin >> s;
    	cin>> k;
    	flag=string_count(s,k);
	    if(flag==-1)
	        cout <<"Case #" << l <<": "<< "IMPOSSIBLE" <<endl;
	    else
	        cout <<"Case #" << l <<": "<< flag << endl;
   }  
   return 0;
}
