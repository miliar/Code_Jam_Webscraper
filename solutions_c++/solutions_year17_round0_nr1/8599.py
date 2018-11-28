#include <bits/stdc++.h>
using namespace std;


int main(int argc, char const *argv[])
{
	long long unsigned K;
	int T, count = 1;
	char str[1005];

	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);

	cin >> T;	
	while(T-- > 0) {
	    cin >> str >> K; 
	    int left = 0, right = strlen(str), flips = 0;
	    while(left < right){	    	
	    	if(str[left] == '-'){
	    		for(int i = 0; i < K; i++){
	    			if(str[left + i] == '-')
	    				str[left+i] = '+';
	    			else
	    				str[left+i] = '-';
	    		}
	    		left++;
	    		flips++;
	    	}
	    	else{
	    		left++;
	    	}
	    	if(str[right] == '-'){
	    		for (int i = 0; i < K; ++i)
	    		{
	    			if(str[right - i] == '-')
	    				str[right-i] = '+';
	    			else
	    				str[right-i] = '-';
	    		}
	    		right--;
	    		flips++;
	    	}
	    	else{
	    		right--;
	    	}
	    }
	    int flag = 0;
	    for(int i = 0; i < strlen(str); i++){
	    	if(str[i] == '-')
	    	{
	    		cout << "Case #" << count++ <<": " << "IMPOSSIBLE" << endl;
	    		flag = 1;
	    		break;
	    	}
	    }
	    if(flag != 1)
	    	cout << "Case #" << count++ <<": " << flips << endl;
	}
	return 0;
}