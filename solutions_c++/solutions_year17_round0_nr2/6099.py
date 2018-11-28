#include <vector>
#include <iostream>

using namespace std;



int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
	
		string s;
		cin >> s;
		int n = s.size();
		
		if(n == 1)
			cout << s[0] << endl;
		else {
			string t = s;
			
			for(int l = 0; l < n; l++)
			{
				bool ok = true;
				int j;
				for(j = n-1; ok && j > 0; j--)
					ok = (t[j] >= t[j-1]);
								
				if(ok)
					continue;

				t[j]--;
				for(int k = j+1; k < n; k++)
					t[k] = '9';
			}
			
			for(int l = 0; l < n; l++)
			if(l > 0 || t[l] != '0')
				cout << t[l];
			cout << endl;
		}
	}
}
