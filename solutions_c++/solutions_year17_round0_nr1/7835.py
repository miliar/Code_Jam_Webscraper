#include <iostream>
#define MAX 1100

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int test=1; test<=t; test++)
	{
		int arr[MAX];
		
		string str;
		cin >> str;
		
		int key;
		cin >> key;
		
		for(int i=0; i<MAX; i++)
            arr[i]=0;
            
        int ans=0;
         
		for(int i = 1; i<=str.length(); i++)
		{
            char current;
            current = str[i-1];
            arr[i] += arr[i-1];
            
            if(arr[i]%2)
            {
                if(current=='+')
                    current='-';
                else
                    current='+';
            }
            
            if(current=='-')
            {
                if(i+key>str.length()+1)
                {
                    ans=-1;
                    break;
                }
                ans++;
                arr[i]++;
                arr[i+key]--;
            }
        }
       
        if(ans==-1)
            cout<< "Case #" << test << ": IMPOSSIBLE" <<endl;
        else
            cout<< "Case #" << test << ':'<<' ' << ans <<endl;
	}
    return 0;
}