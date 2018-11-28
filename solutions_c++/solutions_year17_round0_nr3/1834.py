#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>
#include <cstring>
#include <queue>
#include <iomanip> 

using namespace std;

int trans(int x, int y)
{
	return x * 20 + y;
}

struct state {
	int pos;
	double val;
	int step;
	int bb[20][20];
};


bool aa[20][20];

double handlepos(int x, int y, double p, double q, int bb[20][20])
{
	if (aa[x][y])
	{
		if (bb[x][y] == 0)
		{
			bb[x][y]++;
			return p;
		}
		else
		{
			bb[x][y]++;
			return pow(1 - p, bb[x][y] - 1) * p;
		}
	}
	else
	{
		bb[x][y]++;
		if (bb[x][y] == 1)
		return q;
		else return pow(1 - q, bb[x][y] - 1) * q;
	}
}

void p3(istream &is, ostream &os)
{
	int t;
	is >> t;
	
	for (int i = 1; i <= t; i++)
	{
		double res = 0;
		int r, c, rs, cs, s;
		double q, p;
		is >> r >> c >> rs >> cs >> s;
		is >> p >> q;
		memset(aa, 0, 400);

		for (int j = 0; j < r; j++)
			for (int k = 0; k < c; k++)
			{
				char ch;
				is >> ch;
				if (ch == 'A')
					aa[j][k] = 1;
				else aa[j][k] = false;
			}
	
		queue<state> ss;
		ss.push({ trans(rs, cs), 0, 0 , {} });
		while (!ss.empty())
		{
			state top = ss.front();
			ss.pop();
			if (top.step > s) continue;
			if (top.val > res) 
				res = top.val;
			int rr, cc;
			rr = top.pos / 20;
			cc = top.pos % 20;
			//cout << "pos :" << rr << "," << cc;
			//cout << "val:" << top.val << endl;
			if (rr == 0 && cc == 0)
			{
				state ns;
				if (1 != c)
				{
					ns.pos = 1;
					ns.step = top.step + 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(0, 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != r)
				{
					ns.pos = 20;
					memcpy(ns.bb, top.bb, 1600);
					ns.step = top.step + 1;
					ns.val = top.val + handlepos(1, 0, p, q, ns.bb);
					ss.push(ns);
				}

			}
			else if (rr == r - 1 && cc == c - 1)
			{
				state ns;
				ns.step = top.step + 1;
				if (cc - 1 >= 0)
				{
					ns.pos = (rr) * 20 + cc - 1;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(r - 1, c - 2, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (rr - 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(r - 2, c - 1, p, q, ns.bb);
					ss.push(ns);
				}

			}
			else if (rr == 0 && cc == c - 1)
			{
				state ns;
				ns.step = top.step + 1;
				if (cc - 1 >= 0)
				{
					ns.pos = cc - 1;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(0, c - 2, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != r)
				{
					ns.pos = 20 + c - 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(1, c - 1, p, q, ns.bb);
					ss.push(ns);
				}
			}
			else if (rr == r - 1 && cc == 0)
			{
				state ns;
				ns.step = top.step + 1;
				if (1 != c)
				{
					ns.pos = (r - 1) * 20 + 1;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(r - 1, 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (r - 2) * 20;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(r - 2, 0, p, q, ns.bb);
					ss.push(ns);
				}
			}
			else if (rr == 0)
			{
				state ns;
				ns.step = top.step + 1;
				if (1 != r)
				{
					ns.pos = 20 + cc;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(1, cc, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != c)
				{
					ns.pos = cc + 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(0, cc + 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (cc - 1 >= 0)
				{
					ns.pos = cc - 1;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(0, cc - 1, p, q, ns.bb);
					ss.push(ns);

				}

			}
			else if (rr == r - 1)
			{
				state ns;
				ns.step = top.step + 1;
				if (cc - 1 >= 0)
				{
					ns.pos = (rr) * 20 + cc - 1;
					memcpy(ns.bb, top.bb, 1600);

					ns.val = top.val + handlepos(rr, cc - 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != c)
				{
					ns.pos = rr * 20 + cc + 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr, cc + 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (rr - 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr - 1, cc, p, q, ns.bb);
					ss.push(ns);
				}
			}
			else if (cc == 0)
			{
				state ns;
				ns.step = top.step + 1;
				if (1 != c)
				{
					ns.pos = rr * 20 + 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr, 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (rr - 1) * 20;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr - 1, 0, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != r)
				{
					ns.pos = (rr + 1) * 20;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr + 1, 0, p, q, ns.bb);
					ss.push(ns);
				}
			}
			else if (cc == c - 1)
			{
				state ns;
				ns.step = top.step + 1;
				if (cc - 1 >= 0)
				{
					ns.pos = rr * 20 + cc - 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr, cc - 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (rr - 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr - 1, cc, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != r)
				{
					ns.pos = (rr + 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr + 1, cc, p, q, ns.bb);
					ss.push(ns);
				}

			}
			else
			{
				state ns;
				ns.step = top.step + 1;
				if (cc - 1 >= 0)
				{
					ns.pos = rr * 20 + cc - 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr, cc - 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != c)
				{
					ns.pos = rr * 20 + cc + 1;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr, cc + 1, p, q, ns.bb);
					ss.push(ns);
				}
				if (rr - 1 >= 0)
				{
					ns.pos = (rr - 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr - 1, cc, p, q, ns.bb);
					ss.push(ns);
				}
				if (1 != r)
				{
					ns.pos = (rr + 1) * 20 + cc;
					memcpy(ns.bb, top.bb, 1600);
					ns.val = top.val + handlepos(rr + 1, cc, p, q, ns.bb);
					ss.push(ns);
				}

			}

		}
		os << "Case #" << i << ": "  << setprecision(8) << res << endl;
	}
}


uint64_t caln(uint64_t n, uint64_t m, int i)
{
	uint64_t ret = 0, base = pow(10, m - 1), back = n;
	uint64_t rem = m == 1 ? 0: pow(10, m - 1);
	while (n > rem)
	{
		if (n > i)
			ret += base;
		if (n == i)
			ret += back - base * n + 1;
		base *= 10;
		n /= 10;
	}
	return ret;
}
#include <algorithm>
void baoli(uint64_t n, uint64_t m)
{
	uint64_t d[10][18] = {};
	for (int i = 1; i < 10; i++)
		for (int j = 1; j <= 18; j++)
		{
			d[i][j - 1] = caln(n, j, i);
		}

	for (int i = 1; i < 10; i++)
	{
		for (int j = 0; j < 18; j++)
			cout << d[i][j] << " ";
		cout << endl;
	}
	vector<int> res;
	for (int i = 0; i < 18; i++)
	{
		uint64_t sum = 0;
		int j = 0;
		for (j = 0; j < 10; j++)
		{
			sum += d[j][i];
			if (m <= sum) break;
		}
		res.push_back(j);
	}
	for (auto i : res) cout << i;
	cout << endl;
}
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;


struct office
{
	int no;
	int time;
};

struct stu
{
	int num;
	int t;
	int p;
	vector<office> route;
	int index;
	int res;
};

struct val
{
	int st;
	int num;
	int need, offno;
	int index, total;
	void debug()
	{
		cout << "num" << num << ", st = " << st << ", need = " << need << ", offno = " << offno << endl;
	}
};
class comp
{
public:
	bool operator() (const val &lhs, const val &rhs)
	{
		bool ret;
		if (lhs.st == rhs.st)
			ret = lhs.num > rhs.num;
		else ret = lhs.st > rhs.st;
		return ret;
	}
};
/*
bool busy[101];
int nextfree[101];
int main()
{
	int n, m, k;
	cin >> n >> m >> k;
	map<int, stu> s;
	priority_queue<val, vector<val>, comp> queue;
	for (int i = 0; i < n; i++)
	{
		stu temp;
		cin >> temp.num >> temp.t >> temp.p;
		temp.index = i;
		val v;
		for (int j = 0; j < temp.p; j++)
		{
			office off;
			cin >> off.no >> off.time;
			if (j == 0)
			{
				v.num = temp.num;
				v.need = off.time;
				v.st = temp.t + k;
				v.offno = off.no;
				v.index = 0;
				v.total = temp.p;
				queue.push(v);
			}
			temp.route.push_back(off);
		}
		s[temp.num] = temp;
	}

	while (!queue.empty())
	{
		val temp = queue.top();
		queue.pop();
		temp.debug();
		for (int i = 1; i < 101; i++)
			if (busy[i] && temp.st >= nextfree[i]) busy[i] = false;
		if (temp.index == temp.total) continue;

		if (busy[temp.offno])
		{
			temp.st = nextfree[temp.offno];
			queue.push(temp);
			continue;
		}
		busy[temp.offno] = 1;
		nextfree[temp.offno] = temp.need + temp.st;
		if (temp.index == temp.total - 1)
		{
			s[temp.num].res = temp.need + temp.st;
			temp.st += temp.need;
			temp.index++;
			queue.push(temp);
			continue;
		}
		temp.index++;
		temp.st = temp.st + temp.need + k;
		temp.offno = s[temp.num].route[temp.index].no;
		temp.need = s[temp.num].route[temp.index].time;
		queue.push(temp);

	}

	vector<int> res(n, 0);
	for (map<int, stu>::iterator i = s.begin(); i != s.end(); i++)
		res[i->second.index] = i->second.res;

	for (int i = 0; i < n; i++)
		cout << res[i] << endl;
	system("pause");
}

*/
#include <iostream>
#include <ctime>
#include <cstring>
using namespace std;
int isRec(vector<vector<bool> > rec, int m, int n)
{
	int up = 0, down = 0, left = 0, right = 0;
	for (up = 0; up < n; up++)
	{
		while (left != m && right != m)
		{
			for (left = right; left < m && !rec[left][up]; left++);
			if (left == m) break;
			for (down = up + 1; down < n && !rec[left][down]; down++);
			for (right = left + 1; right < m && !rec[right][up]; right++);
			if (right == m) break;
			if (rec[right][down]) return true;
		}
	}
	return false;
}

void gen(vector<vector<bool> > &rec, int m, int n)
{
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			rec[i][j] = (rand() & 15) == 7;
}


#include <iostream>
#include <ctime>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;
double res[100002];
int uniquePaths(int m, int n) {
	int mm = min(m, n) - 1;
	int nn = m + n - 2;
	double ret = 1.0;
	for (int i = mm + 1; i <= nn; i++)
	{
		ret *= i;
		ret /= nn - i + 1;
		cout << ret << endl;
	}


	return (int)ret;
}
int longestSubstring(string s, int k) {
	if (k == 1) return s.size();
	int *dp = new int[s.size() * 26 + 26];
	int ret = 0;
	memset(dp, 0, sizeof(int) * 26 * (s.size() + 1));
	for (int i = 0; i < s.size(); i++)
	{
		dp[i * 26 + s[i] - 'a' + 26]++;
	}
	for (int i = 1; i <= s.size(); i++)
	{
		for (int j = 0; j < 26; j++)
			dp[i * 26 + j] += dp[i * 26 + j - 26];
	}

	for (int i = 0; i <= s.size() - k; i++)
		for (int j = i + k; j <= s.size(); j++)
		{
			int kk;
			for (kk = 0; kk < 26; kk++)
			{
				if (dp[i * 26 + kk] != dp[j * 26 + kk])
				{
					if (dp[j * 26 + kk] - dp[i * 26 + kk] < k)
						break;
				}
			}
			if (kk == 26)
			{
				while (j != s.size() && dp[j * 26 + s[j] - 'a'] - dp[i * 26 + s[j] - 'a'] > k) j++;
				ret = max(ret, j - i);
				if (j == s.size()) return ret;
			}
		}
	return ret;
}

double maxPossibility(int total, int req, vector<double> pos)
{
	sort(pos.begin(), pos.end());
	double ret = 0;
	for (int i = 0; i < req / 2; i++)
	{
		ret += pos[i] * (1 - pos[total - 1 - i]) + pos[total - 1 - i] * (1 - pos[i]);
	}
	return ret;

}

void printMatrix(vector<vector<int> >& matrix)
{
	int width = matrix.size(), height = matrix[0].size();

	for (int i = 0; i < width; i++)
	{
		for (int j = 0; j < height; j++)
			cout << matrix[i][j] << " ";
		cout << endl;
	}
}


void bfs(vector<vector<int> > &matrix, int width, int height, int begx, int begy)
{
	vector<bool> visit(width * height, false);
	for (int i = 0; i < width * height; i++)
	{
		if (i < height || i > width * height - height || i % height == 0 || i % height == height - 1)
			visit[i] = true;
		else
			visit[i] = false;
	}
	queue<int> q;
	q.push(begx * height + begy);
	while (!q.empty())
	{
		int temp = q.front(), x = temp / height, y = temp % height;
		q.pop();
		visit[temp] = true;

		if (matrix[x + 1][y] && !visit[temp + height])
		{
			matrix[x + 1][y] = min(matrix[x][y] + 1, matrix[x + 1][y]);
			q.push(temp + height);
		}
		if (matrix[x - 1][y] && !visit[temp - height])
		{
			matrix[x - 1][y] = min(matrix[x][y] + 1, matrix[x - 1][y]);
			q.push(temp - height);
		}
		if (matrix[x][y + 1] && !visit[temp + 1])
		{
			matrix[x][y + 1] = min(matrix[x][y] + 1, matrix[x][y + 1]);
			q.push(temp + 1);
		}
		if (matrix[x][y - 1] && !visit[temp - 1])
		{
			matrix[x][y - 1] = min(matrix[x][y] + 1, matrix[x][y - 1]);
			q.push(temp - 1);
		}
		printMatrix(matrix);
		cout << endl;
	}
}

void init(vector<vector<int> >& old, vector<vector<int> >& New)
{
	for (int i = 1; i < old.size() + 1; i++)
		for (int j = 1; j < old[0].size() + 1; j++)
		{
			cout << old.size() << endl;
			New[i][j] = old[i - 1][j - 1];
			if (old[i - 1][j - 1] == 1)
				New[i][j] = 300;
		}
}

/*
vector<vector<int> > updateMatrix(vector<vector<int> >& matrix) {
	if (matrix.size() == 0 || matrix[0].size() == 0) return matrix;
	int width = matrix.size(), height = matrix[0].size();
	vector<vector<int> > help;
	vector<int> initVec(height + 2, 1);
	for (int i = 0; i < width + 2; i++)
		help.push_back(initVec);

	init(matrix, help);
	for (int i = 0; i < width; i++)
		for (int j = 0; j < height; j++)
		{
			if (matrix[i][j] == 0)
				bfs(help, width + 2, height + 2, i + 1, j + 1);
		}
	for (int i = 0; i < width; i++)
		for (int j = 0; j < height; j++)
		{
			matrix[i][j] = help[i + 1][j + 1];
		}
	return matrix;
}



*/




/*
dp[i][j] = 0  if s[i][j] = 0
			min(ÏàÁÚµÄ) + 1 otherwise




*/
#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>

bool isTiny(int64_t in)
{
	int old = 10;
	while (in)
	{
		if (in % 10 > old)
			return false;
		old = in % 10;
		in /= 10;
	}
	return true;
}

int64_t maxTidy(int64_t in)
{
	vector<int> rem;
	while (in)
	{
		rem.insert(rem.begin(), in % 10);
		in /= 10;
	}
	int old = 0;
	for (int i = 0; i < rem.size(); i++)
	{
		if (rem[i] < rem[old])
		{
			break;
		}
		old = i;
	}

	for (int i = old + 1; i < rem.size(); i++)
		rem[i] = 9;

	while (old > 0 && rem[old]-- == rem[old - 1])
	{
		//rem[old]--;
		rem[old] = 9;
		old--;
	}
	if (old == 0)
	{
		rem[0]--;
	}
	int64_t ret = 0;

	for (auto i : rem)
	{
		ret *= 10;
		ret += i;
	}
	return ret;
}

int p1(ifstream& ifs)
{
	string s;
	int k;
	ifs >> s;
	ifs >> k;
	int res = 0;
	for (int i = 0; i <= s.size() - k; i++)
	{
		if (s[i] == '-')
		{
			res++;
			for (int j = 0; j < k; j++)
				if (s[i + j] == '+')
					s[i + j] = '-';
				else s[i + j] = '+';
		}
	}
	cout << s << endl;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '-')
			return -1;
	}
	return res;
}

int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("input1");
	ofs.open("output");

	int T;
	ifs >> T;
	for (int i = 1; i <= T; i++)
	{
		int64_t k, n;
		ifs >> n >> k;
		int64_t M, m;
		map<int64_t, int64_t> num;
		map<int64_t, bool> visit;
		num[n] = 1;
		num[0] = 0;
		for (auto it = --num.end(); it != num.begin(); it--)
		{
			if (!visit[it->first])
			{
				n = it->first;
				visit[n] = true;
				M = (n - 1) / 2 + !(n & 1);
				m = (n - 1) / 2;
				if (num.find(M) != num.end())
					num[M] += num[n];
				else
					num[M] = num[n];
				if (num.find(m) != num.end())
					num[m] += num[n];
				else
					num[m] = num[n];

				it = --num.end();
			}
		}

		for (auto it = --num.end(); it != num.begin(); it--)
		{
			if (it->second >= k)
			{
				M = (it->first - 1) / 2 + !(it->first & 1);
				m = (it->first - 1) / 2;
				break;
			}
			else 
			{
				k -= it->second;
			}
		}

		ofs << "Case #" << i << ": " << M << " " << m << endl;
	}
	//cin >> T;
	return 0;
}

