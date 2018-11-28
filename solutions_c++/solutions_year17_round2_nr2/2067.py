#include <iostream>
#include <limits>
#include <algorithm>
#include <string>

#define create(x, y) x y = read <x>()

using namespace std;

inline void init()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
}

template <typename T>
inline T read()
{
	T temp;
	cin >> temp;
	return temp;
}

template <typename T, typename Y>
inline void print(T case_number, Y answer)
{
	cout << "Case #" << case_number << ": " << answer << '\n';
}

template <typename T, typename S>
inline void getR(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'R';
	alg(n - 1, r - 1, o, y, g, b, v, 1, end, answer);
}

template <typename T, typename S>
inline void getO(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'O';
	alg(n - 1, r, o - 1, y, g, b, v, 2, end, answer);
}

template <typename T, typename S>
inline void getY(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'Y';
	alg(n - 1, r, o, y - 1, g, b, v, 3, end, answer);
}

template <typename T, typename S>
inline void getG(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'G';
	alg(n - 1, r, o, y, g - 1, b, v, 4, end, answer);
}

template <typename T, typename S>
inline void getB(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'B';
	alg(n - 1, r, o, y, g, b - 1, v, 5, end, answer);
}

template <typename T, typename S>
inline void getV(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	answer += 'V';
	alg(n - 1, r, o, y, g, b, v - 1, 6, end, answer);
}

template <typename T, typename S>
inline void alg(T n, T r, T o, T y, T g, T b, T v, T last, T end, S &answer)
{
	switch (last)
	{
	case 1:
		if (n == 0)
		{
			if (end == 6 || end == 1 || end == 2)
				answer = "IMPOSSIBLE";
		}
		else if (g > 0)
			getG(n, r, o, y, g, b, v, last, end, answer);
		else if (y > b || (y == b && (end == 2 || end == 3 || end == 4)))
			getY(n, r, o, y, g, b, v, last, end, answer);
		else if (b > 0)
			getB(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	case 2:
		if (n == 0)
		{
			if (end == 1 || end == 2 || end == 3)
				answer = "IMPOSSIBLE";
		}
		else if (b > 0)
			getB(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	case 3:
		if (n == 0)
		{
			if (end == 2 || end == 3 || end == 4)
				answer = "IMPOSSIBLE";
		}
		else if (v > 0)
			getV(n, r, o, y, g, b, v, last, end, answer);
		else if (r > b || (r == b && (end == 6 || end == 1 || end == 2)))
			getR(n, r, o, y, g, b, v, last, end, answer);
		else if (b > 0)
			getB(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	case 4:
		if (n == 0)
		{
			if (end == 3 || end == 4 || end == 5)
				answer = "IMPOSSIBLE";
		}
		else if (r > 0)
			getR(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	case 5:
		if (n == 0)
		{
			if (end == 4 || end == 5 || end == 6)
				answer = "IMPOSSIBLE";
		}
		else if (o > 0)
			getO(n, r, o, y, g, b, v, last, end, answer);
		else if (y > r || (y == r && (end == 2 || end == 3 || end == 4)))
			getY(n, r, o, y, g, b, v, last, end, answer);
		else if (r > 0)
			getR(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	case 6:
		if (n == 0)
		{
			if (end == 5 || end == 6 || end == 1)
				answer = "IMPOSSIBLE";
		}
		else if (y > 0)
			getY(n, r, o, y, g, b, v, last, end, answer);
		else
			answer = "IMPOSSIBLE";
		break;
	}
}

template <typename T>
inline void test(T case_number)
{
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	string answer;
	if (r > 0)
	{
		answer = "R";
		alg(n - 1, r - 1, o, y, g, b, v, 1, 1, answer);
	}
	else if (y > 0)
	{
		answer = "Y";
		alg(n - 1, r - 1, o, y, g, b, v, 3, 3, answer);
	}
	else if (b > 0)
	{
		answer = "B";
		alg(n - 1, r - 1, o, y, g, b, v, 5, 5, answer);
	}
	else
		answer = "IMPOSSIBLE";
	print(case_number, answer);
}

int main()
{
	init();
	create(int, t);
	for (int i = 1; i <= t; i++)
		test(i);
	return 0;
}