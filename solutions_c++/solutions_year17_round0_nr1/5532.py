#include <iostream>
#include <string>
using namespace std;
void main()
{
	int T, K, x, y, len, spos, pos, i;
	string S;
	cin >> T;
	for(x=1; x<=T; x++)
	{
		cin >> S;
		cin >> K;
		len=S.size();
		y=0;
		pos=S.find('-');
		while(pos!=string::npos)
		{
			if(pos>len-K)
				break;
			for(i=0;i<K;i++)
				S[pos+i]=(S[pos+i]=='-')?'+':'-';
			y++;
			spos=pos;
			pos=S.find('-', spos+1);
		}
		cout << "Case #" << x << ": ";
		if(S.find('-')!=string::npos)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << y << endl;
	}
}