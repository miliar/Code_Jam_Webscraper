#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

void test(){
	string s;
	cin >> s;
	for(int i = 0 ; i < s.length() ; ){
		//cout << i << " " << s << endl;
		int j = i+1;
		while( j < s.length() && s[j] == s[i] ){
			j++;
		}
		if( j == s.length() )
			break;
		if( s[j] > s[i] ){
			i = j;
			continue;
		}
		for(int k = i+1 ; k < s.length() ; k++){
			s[k] = '9';
		}
		s[i]--;
		break;
	}
	if(s[0] == '0')
		s.erase(s.begin());
	cout << s << endl;	
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
