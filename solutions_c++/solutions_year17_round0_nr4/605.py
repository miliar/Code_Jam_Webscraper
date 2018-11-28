
#define PROBLEM_NAME "D"
#define PROBLEM_SMALL_INPUT "-small-attempt6"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <map>

//#define ENABLE_DUMP

char* board = 0;
int N, M;
#define CLEAR_BOARD()		{ delete[] board; board = 0;}
#define INIT_BOARD()		{ delete[] board; board = new char[N*N+1]; for(int __i=0; __i<N*N; ++__i) board[__i]='.'; board[N*N]=0; }
//#define SET_BOARD(r,c,ch)	{ board[N*((r)-1)+((c)-1)]=(ch); }
inline void SET_BOARD(int r, int c, char ch)
{
	int index = N*(r-1)+(c-1);
	if (index < 0 || index >= N*N)
		cerr << "index out of bound : " << r << ", " << c << endl;
	board[index]=ch;
}
#define GET_BOARD(r,c)		board[N*((r)-1)+((c)-1)]

inline int GET_SCORE()
{
	int score = 0;
	for (int i=0; i<N*N; ++i)
	{
		char ch = board[i];
		if (ch == '+' || ch == 'x')
			score+=1;
		else if (ch == 'o')
			score+=2;
	}
	return score;
}

void DUMP_BOARD()
{
#ifdef ENABLE_DUMP
	for (int r=1; r<=N; ++r)
	{
		for (int c=1; c<=N; ++c)
		{
			fout << GET_BOARD(r,c);
		}
		fout << endl;
	}
#endif // ENABLE_DUMP
}

#define GET_BOARD_CHECK(r,c)		{char ch = board[N*((r)-1)+((c)-1)]; if (ch == '+') cnt_plus++; else if (ch == 'x') cnt_x++; else if (ch == 'o') cnt_o++; }
bool CheckBoard(int N, const char* board)
{
	for (int r=1; r<=N; ++r)
	{
		int cnt_plus = 0, cnt_o = 0, cnt_x = 0;
		for (int c=1; c<=N; ++c)
		{
			GET_BOARD_CHECK(r,c);
		}
		if (cnt_plus + cnt_o + cnt_x <= 1)
			continue;
		else if (cnt_o + cnt_x >= 2)
		{
#ifdef ENABLE_DUMP
			fout << "ERROR : Row " << r << " has >2 non-'+' nodes" << endl;
#endif // ENABLE_DUMP
			return false;
		}
	}

	for (int c=1; c<=N; ++c)
	{
		int cnt_plus = 0, cnt_o = 0, cnt_x = 0;
		for (int r=1; r<=N; ++r)
		{
			GET_BOARD_CHECK(r,c);
		}
		if (cnt_plus + cnt_o + cnt_x <= 1)
			continue;
		else if (cnt_o + cnt_x >= 2)
		{
#ifdef ENABLE_DUMP
			fout << "ERROR : Column " << c << " has >2 non-'+' nodes" << endl;
#endif // ENABLE_DUMP
			return false;
		}
	}

	for (int a=-N+1; a<=N-1; ++a)
	{
		int cnt_plus = 0, cnt_o = 0, cnt_x = 0;
		for (int c=1; c<=N; ++c)
		{
			int r = c+a;
			if (r < 1 || r > N)
				continue;
			GET_BOARD_CHECK(r,c);
		}
		if (cnt_plus + cnt_o + cnt_x <= 1)
			continue;
		else if (cnt_o + cnt_plus >= 2)
		{
#ifdef ENABLE_DUMP
			fout << "ERROR : \\ diagonal from [" << 1+a << ", 1] (or [1, " << 1-a << "] ) has >2 non-'+' nodes" << endl;
#endif // ENABLE_DUMP
			return false;
		}
	}

	for (int a=2; a<=2*N; ++a)
	{
		int cnt_plus = 0, cnt_o = 0, cnt_x = 0;
		for (int c=1; c<=N; ++c)
		{
			int r = a-c;
			if (r < 1 || r > N)
				continue;
			GET_BOARD_CHECK(r,c);
		}
		if (cnt_plus + cnt_o + cnt_x <= 1)
			continue;
		else if (cnt_o + cnt_plus >= 2)
		{
#ifdef ENABLE_DUMP
			fout << "ERROR : / diagonal from [" << a-1 << ", 1] (or [6, " << a-6 << "] ) has >2 non-'+' nodes" << endl;
#endif // ENABLE_DUMP
			return false;
		}
	}
	return true;
}

//struct model
//{
//	char ch;
//	int r, c;
//};
//
//typedef vector<model> model_type;
//model_type new_model;
//
//#define GET_CHAR(it)	((*it).ch)
//#define GET_R(it)		((*it).r)
//#define GET_C(it)		((*it).c)

typedef map<pair<int,int>, char> model_type;
model_type new_model;

#define GET_CHAR(it)	((*it).second)
#define GET_R(it)		((*it).first.first)
#define GET_C(it)		((*it).first.second)

int recursive(string& str, int index, int curr_score)
{
	if (index >= str.size())
	{
		fout << "depth " << index << " : " << str << " (score : " << curr_score << ")" << endl;
		return curr_score;
	}

	string str_o = str; str_o[index] = 'o';
	string str_x = str; str_x[index] = 'x';
	string str_p = str; str_p[index] = '+';
	string str_D = str;

	int score_o = CheckBoard(N, &str_o[0]) ? recursive(str_o, index+1, curr_score + 2) : -1;
	int score_x = CheckBoard(N, &str_x[0]) ? recursive(str_x, index+1, curr_score + 1) : -1;
	int score_p = CheckBoard(N, &str_p[0]) ? recursive(str_p, index+1, curr_score + 1) : -1;
	int score_D = CheckBoard(N, &str_D[0]) ? recursive(str_D, index+1, curr_score) : -1;

	if (str_o > str_x && str_o > str_p && str_o > str_D)
	{
		str = str_o;
		return score_o;
	}
	if (str_x > str_o && str_x > str_p && str_x > str_D)
	{
		str = str_x;
		return score_x;
	}
	if (str_p > str_o && str_p > str_x && str_p > str_D)
	{
		str = str_p;
		return score_p;
	}
	if (str_D > str_o && str_D > str_x && str_D > str_p)
	{
		str = str_D;
		return score_D;
	}
	return curr_score;
}

int temp()
{
	N = 3;

	string str(N*N, '.');
	int final_score = recursive(str, 0, 0);
	return final_score;
}


int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

//temp(); return 0;
	map<int, vector<int> > score_set;

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		fin >> N >> M;
		INIT_BOARD();

		for (int i=0; i<M; ++i)
		{
			char ch;
			int r, c;
			fin >> ch >> r >> c;
			SET_BOARD(r,c,ch);
		}

		int original_score = GET_SCORE();
		int earned_score = 0;
		new_model.clear();

#ifdef ENABLE_DUMP
		fout << "original board : " << N << "*" << N << " (score " << original_score << ")" << endl;
		DUMP_BOARD();
#endif ENABLE_DUMP

		// custom codes for small input where all element lie at the row 1.
		if (true)
		{
			vector<pair<int, int> > pos_plus, pos_o, pos_x;
			int r = 1;
			for (int c=1; c<=N; ++c)
			{
				char ch = GET_BOARD(r, c);
				if (ch == '+')
					pos_plus.push_back(make_pair(r, c));
				else if (ch == 'x')
					pos_x.push_back(make_pair(r, c));
				else if (ch == 'o')
					pos_o.push_back(make_pair(r, c));
			}

			// strategy : fill 1st line with '+' except one. that should be filled with 'o'.
			// then, fill diagonal line with 'x'
			//
			// if there is already 'x' in the 1st row,
			//      change it to 'o'
			//      fill other empty cells in the 1st row to '+'
			//      fill diagonal with 'x'
			// else if there is already 'o' in the 1st row
			//      fill other empty cells in the 1st row to '+'
			//      fill diagonal with 'x'
			// else
			//      fill or change 1st cell to 'o'
			//      fill other empty cells in the 1st row to '+'
			//      fill diagonal with 'x'

			int c_o = -1, c_o2 = -1;
			if (!pos_x.empty())
			{
				new_model[make_pair(r, pos_x[0].second)] = 'o';
				SET_BOARD(r,pos_x[0].second,'o');
				c_o = pos_x[0].second;

				if (N>2 && c_o == N)
				{
					new_model[make_pair(N, N-1)] = 'o';
					SET_BOARD(N,N-1,'o');
					c_o2 = N-1;
				}
			}
			else if (!pos_o.empty())
			{
				c_o = pos_o[0].second;

				if (N>2 && c_o == N)
				{
					new_model[make_pair(N, N-1)] = 'o';
					SET_BOARD(N,N-1,'o');
					c_o2 = N-1;
				}
			}
			else
			{
				new_model[make_pair(r, N)] = 'o';
				SET_BOARD(r,N,'o');
				c_o = N;
				if (N>2)
				{
					new_model[make_pair(N, N-1)] = 'o';
					SET_BOARD(N,N-1,'o');
					c_o2 = N-1;
				}
			}

			for (int c=1; c<=N; ++c)
			{
				char ch = GET_BOARD(r, c);
				if (ch == '.')
				{
					new_model[make_pair(r, c)] = '+';
					SET_BOARD(r,c,'+');
				}
			}

			int last_row = 2;
			for (int c=1; c<=N; ++c)
			{
				char ch = GET_BOARD(last_row, c);
				if (ch == '.' && c != c_o && c != c_o2)
				{
					new_model[make_pair(last_row, c)] = 'x';
					SET_BOARD(last_row,c,'x');
					last_row++;
				}
			}

			for (int c=2; c<=N-1; ++c)
			{
				char ch = GET_BOARD(N, c);
				if (ch == '.')
				{
					new_model[make_pair(N, c)] = '+';
					SET_BOARD(N,c,'+');
				}
			}
		}

		CheckBoard(N, board);

		int new_score = GET_SCORE();
		earned_score = new_score - original_score;

		score_set[N].push_back(new_score);

//		fout << "Case #" << cases << ": " << earned_score << " " << new_model.size() << endl;
		fout << "Case #" << cases << ": " << new_score << " " << new_model.size() << endl;
		for (model_type::iterator it = new_model.begin(); it != new_model.end(); ++it)
		{
			char ch = GET_CHAR(it);
			int r = GET_R(it);
			int c = GET_C(it);
			fout << ch << " " << r << " " << c << endl;
		}

#ifdef ENABLE_DUMP
		fout << "modified board : " << "(score " << new_score << ") = earned " << earned_score << endl;
		DUMP_BOARD();
		fout << "-------------" << endl;
#endif ENABLE_DUMP
	}

	CLEAR_BOARD();

/*
	for (auto it = score_set.begin(); it != score_set.end(); ++it)
	{
		fout << (*it).first << ", " << (*it).second[0] << endl;

		for (int i=1; i<(*it).second.size(); ++i)
		{
			if ((*it).second[i] != (*it).second[0])
			{
				int asdf = 1;
			}
		}
	}
//*/
	return 0;
}
