#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <tuple>
#include <utility>
#include <thread>
#include <functional>
#include <cmath>
#include <iomanip>

using namespace std;

// Settings based on Debug / Release
#ifdef _DEBUG
constexpr bool bUseThreads = false;
constexpr bool bReadWriteFromFile = false;
#else
constexpr bool bUseThreads = true;
constexpr bool bReadWriteFromFile = true;
#endif


// The ProblemInstance is where we solve the problem for a given test case
class ProblemInstance
{
private:
	const int test_case; // 1-indexed

	int Ac, Aj;
	int N;
	vector<tuple<int, int, bool>> intervals;
	int answer = -1;
public:
	ProblemInstance( int testcase ) : test_case( testcase ) {}
	void ReadInput( istream& input )
	{
		input >> Ac >> Aj;
		N = Ac + Aj;
		for ( int i = 0; i < N; ++i )
		{
			int a, b;
			input >> a >> b;
			intervals.emplace_back( a, b, i < Ac );
		}
	}
	void CalculateAnswer()
	{
		sort( intervals.begin(), intervals.end() );
		int total[2] = {};
		int free = 0;
		int changes = 0;
		vector<int> implicit[2];
		for ( int i = 0; i < N; ++i )
		{
			auto interval = intervals[i];
			auto previous = intervals[i == 0 ? N - 1 : i - 1];
			bool bCurrent = get<2>( interval );
			bool bPrev = get<2>( previous );
			int space = get<0>(interval) - get<1>( previous );
			if ( space < 0 )
			{
				space += 24 * 60;
			}
			if ( bCurrent == bPrev )
			{
				implicit[bCurrent].push_back(space);
				total[bCurrent] += space;
			}
			else
			{
				changes++;
				free += space;
			}
			total[bCurrent] += get<1>( interval ) - get<0>( interval );
		}
		for ( int i = 0; i < 2; ++i )
		{
			sort( implicit[i].begin(), implicit[i].end() );
		}
		int too_small = -1;
		if ( total[0] + free < 12 * 60 )
		{
			too_small = 0;
		}
		else
		{
			too_small = 1;
		}
		bool other = !too_small;
		while ( total[too_small] + free < 12 * 60 )
		{
			if ( implicit[other].empty() )
			{
				cerr << "ERROR" << endl;
			}
			total[too_small] += implicit[other].back();
			implicit[other].pop_back();
			changes += 2;
		}
		answer = changes;
	}
	void WriteOutput( ostream& output )
	{
		output << "Case #" << test_case << ": " << answer << endl;
	}
};

int main()
{
	// Set up the relevant input/output streams
	ifstream InputFileStream;
	ofstream OutputFileStream;
	if ( bReadWriteFromFile )
	{
		InputFileStream.open( "input.txt" );
		OutputFileStream.open( "output.txt" );
	}
	istream& input = bReadWriteFromFile ? InputFileStream : cin;
	ostream& output = bReadWriteFromFile ? OutputFileStream : cout;

	int T; input >> T;
	if ( !bUseThreads )
	{
		for ( int i = 0; i < T; ++i )
		{
			ProblemInstance Instance( i + 1 );
			Instance.ReadInput( input );
			Instance.CalculateAnswer();
			Instance.WriteOutput( output );
		}
	}
	else
	{
		vector<ProblemInstance> Instances; Instances.reserve( T );
		vector<thread> Threads; Threads.reserve( T );
		for ( int i = 0; i < T; ++i ) Instances.emplace_back( i + 1 );
		for ( int i = 0; i < T; ++i ) Instances[i].ReadInput( input );
		for ( int i = 0; i < T; ++i ) Threads.emplace_back( [ &Instances, i ](){ Instances[i].CalculateAnswer(); } );
		for ( int i = 0; i < T; ++i ) Threads[i].join();
		for ( int i = 0; i < T; ++i ) Instances[i].WriteOutput( output );
	}

	if ( bReadWriteFromFile )
	{
		InputFileStream.close();
		OutputFileStream.close();
	}

	cout << "\nDone" << endl;
	int pause_readme; cin >> pause_readme;
}