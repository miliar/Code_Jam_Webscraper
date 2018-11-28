#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

ifstream fin;
ofstream fout;
struct State {
	ll smallSize;
	ll bigSize;
	ll smallCount;
	ll bigCount;
	ll People;
};

struct MinMax {
	ll min;
	ll max;
};

State* Turn(State* st)
{
	State* res = (State*)malloc(sizeof(State));
	res->smallSize = (st->smallSize - 1) / 2;
	res->bigSize = st->bigSize / 2;
	res->People = st->People - st->bigCount - st->smallCount;
	res->bigCount = 0;
	res->smallCount = 0;
	if ((st->smallSize / 2) == (res->smallSize))
		res->smallCount += st->smallCount;
	else
		res->bigCount += st->smallCount;

	if (((st->smallSize - 1) / 2) == (res->smallSize))
		res->smallCount += st->smallCount;
	else
		res->bigCount += st->smallCount;

	if ((st->bigSize / 2) == (res->smallSize))
		res->smallCount += st->bigCount;
	else
		res->bigCount += st->bigCount;

	if (((st->bigSize - 1) / 2) == (res->smallSize))
		res->smallCount += st->bigCount;
	else
		res->bigCount += st->bigCount;
	
	return res;
}

bool LastTurn(State* st)
{
	if (st->People <= (st->bigCount + st->smallCount))
	{
		return true;
	}

	return false;
}

MinMax* LastTurnResult(State* st)
{
	MinMax* res = (MinMax*)malloc(sizeof(MinMax));
	if (st->bigCount >= st->People)
	{
		res->max = st->bigSize / 2;
		res->min = (st->bigSize - 1) / 2;
	}

	else
	{
		res->max = st->smallSize / 2;
		res->min = (st->smallSize - 1) / 2;
	}

	return res;
}

void Result(ll places, ll people)
{
	if (people == 1)
	{
		fout << places / 2 << " " << (places - 1) / 2 << endl;
		return;
	}

	State* st = (State*)malloc(sizeof(State));
	st->People = people - 1;
	st->bigCount = 1;
	st->smallCount = 1;
	st->bigSize = places / 2;
	st->smallSize = (places - 1) / 2;
	while (!LastTurn(st))
	{
		st = Turn(st);
	}

	MinMax* res = LastTurnResult(st);
	fout << res->max << " " << res->min << endl;
}

int main()
{
	fin.open("C-large.in");
	fout.open("output.txt");
	ll T;
	fin >> T;
	for (ll t = 0; t < T; t++)
	{
		fout << "Case #" << t + 1 << ": ";
		ll n, k;
		fin >> n >> k;
		Result(n, k);
	}

	return 0;
}