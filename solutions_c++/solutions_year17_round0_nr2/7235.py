#include <iostream>
#include <cstdio>
using namespace std;
bool check(string n){
    int len=n.length();
        for(int i=1;i<len;i++)
            if(n[i-1]>n[i])
                return false;
        return true;
}
int main() 
{
	freopen("input_file_name.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;cin>>t;
	int c=1;
	while(t--){
	    string arr;
	    cin>>arr;
	    int len=arr.length();
	    while(check(arr)!=true){
	        for(int i=1;i<len;i++){
                    if(arr[i-1]>arr[i])
                    {
                        arr[i-1]= (char)(arr[i-1]-1);

                        for(int j=i;j<len;j++)
                            arr[j]='9';
                    }
                }
	    }
	    printf("Case #%d: ",c++);
	    for(int i=0;i<len;i++)
            if(arr[i]=='0')
                continue;
            else printf("%c",arr[i]);
        printf("\n");
	    
	}
	return 0;
}

