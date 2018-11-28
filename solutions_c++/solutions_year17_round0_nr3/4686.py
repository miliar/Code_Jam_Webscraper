#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
__int64 * solve(__int64 n, __int64 k);
void main() {
	int t;
	__int64 n;
	__int64 k;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;
		__int64 *te;
		te = solve(n, k);
		cout << "Case #" << i << ": " << te[0] << " " << te[1] << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

__int64*  solve(__int64 stallsCount, __int64 user)
{
	__int64 r[2];
	if (stallsCount == user) {
		r[0] = 0;
		r[1] = 0;
		return r;
	}
	__int64 n = stallsCount - 1;
	__int64 a = n / 2;
	__int64 b = n - a;

	__int64 k = user - 1;
	__int64	ka = k / 2;
	__int64 kb = k - ka;

	if (user == 1) {
		r[0] = b;
		r[1] = a;
		return r;
	}
	if (user == 2) {
		return solve(b, 1);
	}

	if (n % 2 == 0) {
		return solve(b, kb);
	}
	else {
		if ( k % 2 == 0) 
		{
			return solve(a, ka);
		}
		else
		{
			return solve(b, kb);
		}
	}
	




}

/*
__int64*  solve(__int64 n, __int64 k)
{
__int64 r[2];
if (n == k)
{
r[0] = 0;
r[1] = 0;
return r;
}
if (k == 1)
{
__int64 temp = n / 2;
r[0] = temp;
if (n % 2 == 0) {
r[1] = temp - 1;
}
else {
r[1] = temp ;
}

return r;
}
if (k < 1) {
cout << "error " << endl;
return r;
}
__int64 temp = n / 2;
if (n % 2 == 0) {
if (k % 2 == 0){
return solve(temp, k - 1);
}
else{
return solve(temp, k/2 -1);
}

}
else {
if (k % 2 == 0) {
return solve(temp + 1, k/2 - 1);
}
else {
return solve(temp + 1, k/2 -1);
}

}

}
*/