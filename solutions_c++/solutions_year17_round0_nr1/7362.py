#include <iostream>
#include <string>

using namespace std;

const char H = '+';
const char B = '-';
const char* IMPOSSIBLE = "IMPOSSIBLE\n";

void flip( string& s, int from, int to )
{
	for( int i = from; i != to; ++i )
	{
		switch( s[i] )
		{
		case '+':
			s[i] = '-';	
		break;
		case '-':
			s[i] = '+';
		break;
		default:
		break;
		}	
	}
}

void solve1( string S, int K, int t )
{
	int N = S.size() - K + 1;
	int flips = 0;
	for( int i = 0; i != N; ++i )
	{
		if( S[i] == '-' )
		{
			S[i] = '+';
			flip( S, i + 1, i + K );
			++flips;
		}	
	}

	bool valid = true;
	for( int i = 0; i != S.size(); ++i )
	{
		if( S[i] != '+' )
		{
			valid = false;
			break;
		}
	}

	cout << "Case #" << t << ": ";

	if( valid )
	{
		cout << flips << '\n';	
	}
	else
	{
		cout << IMPOSSIBLE;
	}
}


int main( int argc, const char* args[] )
{
	int T = 0;
	int K = 0;
	string S;

	cin >> T;
	for( int i = 0; i != T; ++i )
	{
		cin >> S;
		cin >> K;
		solve1( S, K, i + 1 );
	}

	return 0;
}
