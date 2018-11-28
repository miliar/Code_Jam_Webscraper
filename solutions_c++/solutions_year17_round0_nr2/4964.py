#include <iostream>
#include <string>
using namespace std;

bool isTidy(long long val) {
	int n = val%10;
	val /= 10;
	while(val) {
		if (n < val % 10)
			return false;
		n = val%10;
		val /= 10;
	}
	return true;
}

int main() {
	int T;	cin>>T;
	for (int t = 1; t <= T; ++t) {
		string N;	cin>>N;
		cout<<"Case #"<<t<<": ";
		if (isTidy(stoll(N))) {
			cout<<N<<endl;
		} else {
			int len = N.length();
			int i = 0;
			for (; i < len-1; ++i)
				if (N[i] > N[i+1])
					break;
			while (i && N[i] == N[i-1])
				i--;
			
			N[i]--;
			for (int j = i+1; j < len; ++j)
				N[j] = '9';
			if (N[0] != '0')
				cout<<N[0];
			for (int i = 1; i <len; ++i)
				cout<<N[i];
			cout<<endl;
		}
	}
	
	return 0;
}
