#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool isnice(string &s)
{
	for (int i = 0; i < s.length()-1; i++) {
		if (s[i] > s[i+1])
			return false;
	}

	return true;
}

string brutus(string &s) {
	stringstream ss(s);
	ll n; ss >> n;

	for (ll i = n; i>=0; i--) {
		ss = stringstream("");
		ss << i;
		string nro = ss.str();
		if (isnice(nro))
			return nro;
	}

	return "0";
}

bool fixstr(string &s, string &res, int pos, char min) {
	if (pos == s.length()-1)
		return true;

	res[pos] = s[pos];
	if (s[pos] > s[pos+1]) {
		if (s[pos] == min)
			return false;
		res[pos]--;
		for (int j = pos+1; j < s.length(); j++)
			res[j] = '9';
		return true;
	} else {
		if (fixstr(s, res, pos+1, max(min, res[pos])))
			return true;
		if (res[pos] == min)
                        return false;
		res[pos]--;
                for (int j = pos+1; j < s.length(); j++)
                        res[j] = '9';
		return true;
	}
}

string br;

string proc()
{
	string nr;
	cin >> nr;

	string w(nr);
	//br = brutus(nr);

	if (fixstr(nr, w, 0, '0'))
		return w.substr(w.find_first_not_of("0"));

	return string(w.length()-1, '9');
}

int main()
{
	ll T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		string res = proc();
		//cout << "BR " << br << " FAST " << res << endl;
		//assert(br == res);
		//assert(isnice(res));
		cout << "Case #" << i << ": " << res << endl;
	}
}
