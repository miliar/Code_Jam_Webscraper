
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

long findFirstBlank(string s)
{
    int index = s.length();
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
            index = i;
            break;
        }
    }
    return index;
}

int main()
{
    ifstream fin("A-large.in");
	ofstream fou("A-large.out");
    int T,K;
    string S;
    fin>>T;
    for (int i = 1; i <= T; i++) 
	{
        fin>>S>>K;
        int num = 0;
		int p = findFirstBlank(S);
		while (S.length() - p >= K) {
			for (int i = p; i < p + K; i++) 
			{
				if (S[i] == '+') 
				{
					S[i] = '-';
				}
				else
				{
					S[i] = '+';
				}
			}
			p = findFirstBlank(S);
			num++;
		}
		if (p == S.length()) {
			fou<<"Case #"<<i<<": "<<num<<endl;
		}
		else
		{
			fou<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}

    }
    return 0;
}

