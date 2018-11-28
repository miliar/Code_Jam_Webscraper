    #include <iostream>
    #include <string>
     
    using namespace std;
     
    int main() {
    	int t;
    	cin >> t;
    	for(int i = 0; i < t; i++)
    	{
    	    bool impo = false;
    	    int f = 0;
    		int k;
    		string s;
    		cin >> s >> k;
    		int j;
    		for(j = 0; j < s.length()-k+1; j++)
    		{
    			if(s[j] == '-')
    			{
    				for(int m = j; m < j+k; m++)
    				{
    					if(s[m] == '-')
    						s[m] = '+';
    					else
    						s[m] = '-';
    				}
    				f++;
    			}
    		}
    		for(j; j < s.length(); j++)
    		{
    		    if(s[j] == '-')
    		    {
    		        cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    		        impo = true;
    		        break;
    		    }
    		}
    		if(impo == false)
    		    cout << "Case #" << i+1 << ": " << f << endl;
    	}
    	return 0;
    }