#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector< char > VC;
typedef vector< VC > VVC;

//#define DEBUG

#ifdef DEBUG
#define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)
void DE_MATRIX(VVC &m) {
    for (VVC::iterator mit = m.begin(); mit != m.end(); ++mit)
    {
        VC &vrow = *mit;
        for (VC::iterator rowit = vrow.begin(); rowit != vrow.end(); ++rowit)
            DE("%c", *rowit);
        DE("\n");
    }
}
#else
#define DE(format, ...)
#define DE_MII(m)
#endif

bool isLegal(VVC m, int N, int row, int col) {
    {
        int non_conform = 0;
        for (int i = 0; i<N; i++) {
            if ('.' == m[row][i]) continue;
            if ('+' != m[row][i]) ++non_conform;
        }
        if (non_conform > 1)
            return false;
    }
    
    {
        int non_conform = 0;
        for (int i = 0; i<N; i++) {
            if ('.' == m[i][col]) continue;
            if ('+' != m[i][col]) ++non_conform;
        }
        if (non_conform > 1)
            return false;
    }

    {
        int non_conform = 0;
        int minrowcol = min(row, col);
        int r = row - minrowcol;
        int c = col - minrowcol;
        while (r < N && c < N) {
            if ('.' != m[r][c] && 'x' != m[r][c]) ++non_conform;
            ++r; ++c;
        }
        if (non_conform > 1)
            return false;
    }

    {
        int non_conform = 0;
        int minrowcol = min(row, N-1-col);
        int r = row - minrowcol;
        int c = col + minrowcol;
        while (r < N && c >= 0) {
            assert(r >= 0 && c < N);
            if ('.' != m[r][c] && 'x' != m[r][c]) ++non_conform;
            ++r; --c;
        }
        if (non_conform > 1)
            return false;
    }

    return true;
}
    
void solve()
{
	int N, M;
	scanf("%d %d", &N, &M);
	DE("N=%d M=%d\n", N, M);
    VVC matrix(N);
    for (int i = 0; i < N; ++i) {
        matrix[i].resize(N);
        for (int j = 0; j < N; j++)
            matrix[i][j] = '.';
    }
    for (int i = 0; i < M; ++i) {
        char fashion;
        int row, col;
        char tmp_buff[1000];

        // remove previous newline
        fgets(tmp_buff, 1000, stdin);
        scanf("%c %d %d", &fashion, &row, &col);

        assert('x' == fashion || '+' == fashion || 'o' == fashion);
        assert(row <= N && col <= N);
        matrix[row-1][col-1] = fashion;
    }
    
    VVC matrix_orig = matrix;

//#define DEBUG_MATRIX
#ifdef DEBUG_MATRIX
    DE("Orig matrix:\n"); DE_MATRIX(matrix_orig);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            assert(isLegal(matrix_orig, N, i, j));
#endif

    int oj = -1;
    for (int i = 0; i < N; i++) {
        if ('x' == matrix[0][i] || 'o' == matrix[0][i]) {
            oj = i;
        }
    }
    if (-1 == oj) {
        oj = 0;
    }
    
    for (int j = 0; j < N; j++)
        matrix[0][j] = '+';
    matrix[0][oj] = 'o';

    if (N-1 != oj) {
        for (int j = 0; j < oj; j++) {
            assert('.' == matrix[1+j][j]);
            matrix[1+j][j] = 'x';
        }
        for (int j = oj+1; j < N; j++) {
            assert('.' == matrix[j][j]);
            matrix[j][j] = 'x';
        }
    } else {
        // special case - o in top rightmost position
        for (int j = 0; j < N-1; j++) {
            assert('.' == matrix[N-1-j][j]);
            matrix[N-1-j][j] = 'x';
        }
    }

    for (int j = 1; j < N-1; j++) {
        assert('.' == matrix[N-1][j]);
        matrix[N-1][j] = '+';
    }

#ifdef DEBUG_MATRIX
    DE("New matrix:\n"); DE_MATRIX(matrix);
#endif
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            assert(isLegal(matrix, N, i, j));

	
    int result = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if ('+' == matrix[i][j] || 'x' == matrix[i][j]) ++result;
            else if ('o' == matrix[i][j]) result += 2;
            else assert('.' == matrix[i][j]);
        }
    }
    if (1 == N) {
        assert(2 == result);
    } else {
        assert(3*N-2 == result);
    }

    int change_cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (matrix[i][j] != matrix_orig[i][j]) {
                change_cnt++;
            }
        }
    }

#ifdef DEBUG
	DE("result = %d\n", result);
   	printf("%d\n", result);

#else
	DE("result = %d changes=%d\n", result, change_cnt);
	printf("%d %d\n", result, change_cnt);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (matrix[i][j] != matrix_orig[i][j]) {
                printf("%c %d %d\n", matrix[i][j], i+1, j+1);
            }
        }
    }
#endif
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
