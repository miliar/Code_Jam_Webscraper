#include <stdio.h>
#include <unordered_map>
#include <string>
#include <stdlib.h>
#include <string.h>

using namespace std;

void printBinary( int64_t n, int64_t cnt )
{
	string res = "";
	while ( n != 0 ) {
		res = (((n&1)==0)?"0":"1") + res;
		n = n >>1;
	}
	if ( res.length() == 0 ) {
		res = "0";
	}
	
	while ( res.length() < (size_t) cnt ) res = "0" + res;
	
	printf( "%s", res.c_str() );
}

int BFS( int64_t start, int64_t len, int64_t K )
{
	int64_t maxbit = -1;
	maxbit = maxbit << len;
	
	int64_t flipper = 0;
	int64_t i;
	for ( i = 0; i < K; i++ ) {
		flipper = flipper << 1;
		flipper = flipper | 1;
	}
	
	
	unordered_map<int64_t, int64_t> all;
	unordered_map<int64_t, int64_t>* curr = new unordered_map<int64_t, int64_t>();
	unordered_map<int64_t, int64_t>* next = new unordered_map<int64_t, int64_t>();
	unordered_map<int64_t, int64_t>* tmpum;
	
	(*curr)[start] = 0;
	all[start] = 0;
	int64_t cstate;
	
	int curr_gen = 0;
	size_t prev_all_cnt = 0;
	while ( true ) {
		fprintf( stderr, "%d gen done.\n", curr_gen );
		curr_gen++;
		next->clear();
		for ( auto itr = curr->begin(); itr != curr->end(); itr++ ) {
			if ( itr->first == 0 ) {
				return itr->second;
			}
			
			for ( i = flipper; (i & maxbit) == 0; i = i << 1 ) {
				//if ( ( itr->first & i ) == 0 ) continue;
				
				cstate = itr->first ^ i;
				if ( all.count(cstate) == 0 ) {
					(*next)[cstate] = curr_gen;
					all[cstate] = curr_gen;
					/*printf( "Adding: " );
					printBinary( cstate, len );
					printf( " (%d)\n", curr_gen );*/
				}
			}
		}
		
		tmpum = curr;
		curr = next;
		next = tmpum;
		
		if ( all.size() == prev_all_cnt ) return -1;
		prev_all_cnt = all.size();
	}
}

int doSolve( int case_num )
{
	fprintf( stderr, "Running case %d\n", case_num );
	
	int K;
	char inarr[1024];
	scanf( " %s %d", inarr, &K );
	
	int64_t alen = strlen(inarr);
	int64_t i;
	int64_t resn = 0;
	for ( i = 0; i < alen; i++ ) {
		resn = resn << 1;
		if ( inarr[i] == '-' ) {
			resn = resn | 1;
		}
	}
	
	int res = BFS( resn, alen, K );
	printf( "Case #%d: ", case_num );
	if ( res == -1 ) printf( "IMPOSSIBLE\n" );
	else printf( "%d\n", res );
	
	return res;
}

	
int main()
{
	int ccnt;
	scanf( " %d", &ccnt );
	for ( int i = 0; i < ccnt; i++ ) {
		doSolve( i+1 );
	}
	return 0;
}
