#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <utility>
#include <cmath>
#include <memory>
#include <regex>
#include <functional>
#include <tuple>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <iterator>
#include <experimental/iterator>

#ifndef NDEBUG
#define debug(...) WriteLine("> ", __VA_ARGS__, " ~", __LINE__ ,"~")
#define named(x) '[', #x, ": ", x, "] "
#else
#define debug(...)
#endif

using namespace std;
using lint = long long;
using ulint = unsigned long long;

#define span(x) begin(x), end(x)
#define rev_span(x) rbegin(x), rend(x)
#define span_n(x, n) begin(x), advance(x, n)

template<class... Args> using HashSet = unordered_set<Args...>;
template<class... Args> using HashMap = unordered_map<Args...>;
template<class... Args> using Unique = unique_ptr<Args...>;
template<class... Args> using Shared = shared_ptr<Args...>;
template<class... Args> using Matrix = vector<vector<Args...>>;
template<class... Args> constexpr auto make_matrix(size_t rows) { return Matrix<Args...>(rows); }
template<class... Args> constexpr auto make_matrix(size_t rows, size_t columns) { return Matrix<Args...>(rows, vector<Args...>(columns)); }
template<class T, class Distance> constexpr T* advance(T* array, Distance n) noexcept { return array + n; }

template<class T> T Read() { T in; cin >> in; return in; }
template<class... Args> auto Read(Args&... args) { (cin >> ... >> args); }
template<class Iter> auto ReadVec(Iter begin, Iter end) { for_each(begin, end, [](auto& x) { Read(x); }); }
template<class Vec> auto ReadVec(Vec&& vec) { ReadVec(span(vec)); return forward<Vec&&>(vec); }
template<class Mat> auto ReadMat(Mat&& mat) { for(auto& row : mat) { ReadVec(row); } return forward<Mat&&>(mat); }
auto ReadLine() { while(isspace(cin.peek())) cin.ignore(); string line;	getline(cin, line);	return line; }
template<class... Args> auto Write(const Args&... args) { (cout << ... << args); }
template<class... Args> auto WriteLine(const Args&... args) { Write(args..., '\n'); }
template<class Iter> auto WriteVec(Iter begin, Iter end, const string& separator = " ") { copy(begin, end, experimental::make_ostream_joiner(cout, separator)); }
template<class Vec> auto WriteVec(const Vec& vec, const string& separator = " ") { WriteVec(span(vec), separator); }
template<class Mat> auto WriteMat(const Mat& mat) { for(const auto& row : mat) { WriteVec(row); WriteLine(); } } 
auto FormatFloatingPoint(int precision) { cout << fixed << setprecision(precision); }

template<class T = int, bool isReversed = false> struct ExclusiveRange
{
	const T itsBegin, itsEnd;
	
	struct Iterator
	{
		T i;
		auto operator * () const { return i; }
		auto operator ++ () {  if constexpr(isReversed) --i; else ++i; }
		auto operator != (const Iterator& other) const { if constexpr(isReversed) return i > *other; else return i < *other; }
	};
	
	template<class A, class B> ExclusiveRange(const A& itsBegin, const B& itsEnd) : itsBegin{static_cast<T>(itsBegin)}, itsEnd{static_cast<T>(itsEnd)} {}
	Iterator begin() const { return {itsBegin}; }
	Iterator end() const { return {itsEnd}; }
};
constexpr auto range(auto begin, auto end) { return ExclusiveRange<decltype(begin)>{begin, end}; }
constexpr auto rev_range(auto begin, auto end) { return ExclusiveRange<decltype(begin), true>{begin-1, end-1}; }
constexpr auto inclusive_range(auto begin, auto end) { return ExclusiveRange<decltype(begin)>{begin, end+1}; }
constexpr auto rev_inclusive_range(auto begin, auto end) { return ExclusiveRange<decltype(begin), true>{begin, end-1}; }

const auto alphabet = inclusive_range('a', 'z');
const auto Alphabet = inclusive_range('A', 'Z');
const auto Impossible = "IMPOSSIBLE"s;

void SolveCase(int caseId);
int main()
{
	FormatFloatingPoint(6);
	for(auto caseId : inclusive_range(1, Read<int>()))
		SolveCase(caseId);
}

void SolveCase(int caseId)
{
	debug("begin ", named(caseId));
	int N, P;
	Read(N, P);
	int G[] = {0, 0, 0, 0};
	for(auto i : range(0, N))
	{
		 auto c = Read<int>() % P;
		 ++G[c];
	}
	
	int result = G[0];
	
	if(P == 2)
	{
		result += (G[1]/P) + (G[1]%P);
	}
	else if(P == 3)
	{
		auto pairCount = min(G[1], G[2]);
		result += pairCount;
		G[1] -= pairCount;
		G[2] -= pairCount;
		result += (G[1]/P) + ((G[1]%P) ? 1 : 0);
		result += (G[2]/P) + ((G[2]%P) ? 1 : 0);
	}
	else
	{
		
	}

	
	WriteLine("Case #", caseId, ": ", result);
}
