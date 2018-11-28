#include <cstdio>
#include <map>
 
typedef std::pair<int, int> pos;
typedef std::pair<pos, pos> chkpos;
typedef std::map<pos, char> zmap;
typedef std::map<pos, char>::const_iterator zmapciter;
 
char mat[101][101];
bool xmat[101][101];
bool pmat[101][101];
 
inline char ValueMat(const pos& p) {
	return mat[p.first][p.second];
}
inline bool ValueXMat(const pos& p) {
	return xmat[p.first][p.second];
}
inline bool ValuePMat(const pos& p) {
	return pmat[p.first][p.second];
}
inline void SetMat(const pos& p, char S) {
	mat[p.first][p.second] = S;	
}
inline void SetXMat(const pos& p) {
	xmat[p.first][p.second] = true;	
}
inline void SetPMat(const pos& p) {
	pmat[p.first][p.second] = true;	
}
 
 
inline int Min(int a, int b) {
	return a < b ? a : b;
}
inline int Max(int a, int b) {
	return a > b ? a : b;
}
inline int Min(const pos& p) {
	return Min(p.first, p.second);
}
inline int Max(const pos& p) {
	return Max(p.first, p.second);
}
 
inline chkpos GetCheckPosX(const pos& P) {
	chkpos res;
	res.first = pos(P.first, 0);
	res.second = pos(0, P.second);
	return res;
}
 
inline chkpos GetCheckPosP(const pos& P, int N) {
	chkpos res;
	int min = Min(P);
	res.first = pos(P.first - min, P.second - min);
	min = Min(P.first - 1, N - P.second);
	res.second = pos(P.first - min, P.second + min);
	return res;
}
 
inline bool CanAddX(const pos& P) {
	chkpos ref = GetCheckPosX(P);
	return ValueMat(P) != 'x' &&  ValueMat(P) != 'o' &&
	ValueXMat(ref.first) == false && ValueXMat(ref.second) == false;
}
 
inline bool CanAddP(const pos& P, int N) {
	chkpos ref = GetCheckPosP(P, N);
	return ValueMat(P) != '+' &&  ValueMat(P) != 'o' &&
	ValuePMat(ref.first) == false && ValuePMat(ref.second) == false;
}
 
inline char AddX(const pos& P) {
	if( CanAddX(P) == false ) {
		return -1;
	}
	char res = ValueMat(P) == '+'? 'o' : 'x'; 
	SetMat(P, res);
	chkpos ck = GetCheckPosX(P);
	SetXMat(ck.first);
	SetXMat(ck.second);
	return res;
}
inline char AddP(const pos& P, int N) {
	if( CanAddP(P, N) == false ) {
		return -1;
	}
	char res = ValueMat(P) == 'x'? 'o' : '+'; 
	SetMat(P, res);
	chkpos ck = GetCheckPosP(P, N);
	SetPMat(ck.first);
	SetPMat(ck.second);
	return res;
}
 
void ProcessX(int& score, zmap& z, int rs, int re, int cs, int ce)
{
	for( int r = rs; r <= re; r++ ) {
		for( int c = cs; c <= ce; c++ ) {
			pos curpos(r,c);
			char cur = AddX(curpos);
			if( cur < 0 ) {
				continue;
			}
			z[curpos] = cur;
			score++;
		}
	}
}
 
void ProcessP(int& score, zmap& z, int rs, int re, int cs, int ce, int N)
{
	for( int r = rs; r <= re; r++ ) {
		for( int c = cs; c <= ce; c++ ) {
			pos curpos(r,c);
			char cur = AddP(curpos, N);
			if( cur < 0 ) {
				continue;
			}
			z[curpos] = cur;
			score++;
		}
	}
}
 
int main() {
	int T, N, M, R, C;
	char S;
	scanf("%d", &T);
	for( int t = 1; t <= T; t++ ) {
		int score = 0;
		scanf("%d %d", &N, &M);
		// init matrices
		for( int r = 0; r <= N; r++ ) {
			for( int c = 0; c <= N; c++ ) {
				mat[r][c] = '.';
				xmat[r][c] = false;
				pmat[r][c] = false;
			}
		}
		// apply M lines
		for( int i = 1; i <= M; i++ ) {
			while(getchar() != '\n');
			scanf("%c %d %d", &S, &R, &C);
			if( S != '+' ) {
				AddX(pos(R,C));
				score++;
			} 
			if( S != 'x' ) {
				AddP(pos(R,C), N);
				score++;
			}
		}
		// go go go
		zmap zz;
		// go X for all matrix
		ProcessX(score, zz, 1, N, 1, N);
		// go P for all edge
		ProcessP(score, zz, 1, 1, 1, N, N);
		ProcessP(score, zz, N, N, 1, N, N);
		ProcessP(score, zz, 2, N-1, 1, 1, N);
		ProcessP(score, zz, 2, N-1, N, N, N);
 
		printf("Case #%d: %d %d\n", t, score, zz.size());
		zmapciter it;		
		zmapciter itBegin = zz.cbegin();		
		zmapciter itEnd = zz.cend();
		for( it = itBegin; it != itEnd; ++it ) {
			printf("%c %d %d\n", it->second, it->first.first, it->first.second);
		}
	}
	return 0;
}
