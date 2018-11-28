#include <iostream>
#include<string.h>
#include<cstdlib>
using namespace std;

int main() 
{
	int tests;
	int counter = 1;
	cin >> tests;
	while(tests > 0)
	{
	    string strl;
	    cin >> strl;
	    if(strl.size() == 1)
	    {
	        cout << "Case #" << counter << ": " << strl << endl;
	        tests--;
		    counter++;
	        continue;
	    }
	    int flag = 1;
	    for(int i = 0; i < strl.size()-1; i++)
	    {
	        if(strl[i+1] < strl[i])
	        {
	            flag = 0;
	            break;
	        }
	    }
	    int i = strl.size();
	    while(flag == 0)
	    {
	        strl[i] = '9';
	        i--;
	        strl[i]--;
	        flag =1;
	        for(int l = 0; l < strl.size()-1; l++)
	        {
    	        if(strl[l+1] < strl[l])
    	        {
    	            flag = 0;
    	            break;
    	        }
	        }
	    }
	    if(strl[0] == '0')
	    {
	       cout << "Case #" << counter << ": ";
	       for(int k = 1; k < strl.size(); k++)
	       {
		 cout << strl[k];
	       }
	       cout << endl;
	       counter++;
	       tests--; continue;
	    }
	    cout << "Case #" << counter << ": "<< strl << endl;
	    counter++;
	    tests--;
	}
	return 0;
}

