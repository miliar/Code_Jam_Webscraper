#include "cstring"
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (100)
#define N_MAX   (100 + 1)
#define C_MAX   (100)
#define M_MAX   ((N_MAX) * (N_MAX))


#define	DENY_P  (0x1 << 0)
#define	DENY_X  (0x1 << 1)
#define	DENY_O	(0x1 << 2)

struct mdb_s
{
	uint32 N, M;

	char	MM[N_MAX][N_MAX];
	uint8	FF[N_MAX][N_MAX];
	uint8   PP[N_MAX][N_MAX];	/* processed */

	uint32	points, models;

	char	as[M_MAX];
	uint32	ar[M_MAX];
	uint32	ac[M_MAX];
};


#if 1
int traverse_mark_flags(struct mdb_s *pMdb, uint32 R, uint32 C, char Chr)
{
	uint32 r, c;
	uint32 N;
	uint32 oldPoint;

	N = pMdb->N;

	switch (pMdb->MM[R][C])
	{
	case 'o':
		oldPoint = 2;
		break;

	case '+':
	case 'x':
		oldPoint = 1;
		break;

	default:
		oldPoint = 0;
		break;
	}

	//printf("{DBG} oldPoint = %u\n", oldPoint);

	/* update content */
	//printf("{DBG} RC[%u][%u]: %c -> %c\n", R, C, pMdb->MM[R][C], Chr);
	
	pMdb->MM[R][C] = Chr;
	pMdb->as[pMdb->models] = Chr;
	pMdb->ar[pMdb->models] = R;
	pMdb->ac[pMdb->models] = C;
	pMdb->models += 1;

	switch (Chr)
	{
	case 'o':
		pMdb->points += (2 - oldPoint);
	
		/* self[R][C]				=> deny `x`, `+` */
		/* row, column, diagonal	=> deny `o` (cannot be more than one `o`)*/
		/* row, column				=> deny `x` (only able to put `+`) and `o` */
		/* diagonal 				=> deny `+` (only able to put `x`) and `o` */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (o) : r = %u, c = %u \n", r, c);
				
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X, +)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X | DENY_P);
					continue;
				}
	
				/* row, column scan */
				if ((c == C) || (r == R))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (O, X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_X);
				}
	
				/* diagonal scan */
				if (((r + c) == (R + C)) || ((r - c) == (R - C)))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (O, +)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_P);
				}
			}
		}
		break;
	
	case '+':
		pMdb->points += (1 - oldPoint);
	
		/* self[R][C]				=> deny `x` */
		/* diagonal 				=> deny `+` (only able to put `x`) */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (+) : r = %u, c = %u \n", r, c);
	
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X);							
					continue;
				}
	
				/* diagonal scan */
				if (((r + c) == (R + C)) || ((r - c) == (R - C)))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (+)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_P);
				}
			}
		}
		break;
	
	case 'x':
		pMdb->points += (1 - oldPoint);
		
		/* self[R][C]				=> deny `+` */
		/* row, column				=> deny `x` (only able to put `+`) and `o` */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (x) : r = %u, c = %u \n", r, c);
				
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (+)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_P);							
					continue;
				}
	
				/* row, column scan */
				if ((c == C) || (r == R))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_X);
				}
			}
		}
		break;
	
	default:
		break;
	}

	return 0;
}
#else

int traverse_mark_flags(struct mdb_s *pMdb, uint32 R, uint32 C, char Chr)
{
	uint32 r, c;
	uint32 N;
	uint32 oldPoint;

	N = pMdb->N;

	switch (pMdb->MM[R][C])
	{
	case 'o':
		oldPoint = 2;
		break;

	case '+':
	case 'x':
		oldPoint = 1;
		break;

	default:
		oldPoint = 0;
		break;
	}

	//printf("{DBG} oldPoint = %u\n", oldPoint);

	/* update content */
	//printf("{DBG} RC[%u][%u]: %c -> %c\n", R, C, pMdb->MM[R][C], Chr);
	
	pMdb->MM[R][C] = Chr;
	pMdb->as[pMdb->models] = Chr;
	pMdb->ar[pMdb->models] = R;
	pMdb->ac[pMdb->models] = C;
	pMdb->models += 1;

	switch (Chr)
	{
	case 'o':
		pMdb->points += (2 - oldPoint);
	
		/* self[R][C]				=> deny `x`, `+` */
		/* row, column, diagonal	=> deny `o` (cannot be more than one `o`)*/
		/* row, column				=> deny `x` (only able to put `+`) and `o` */
		/* diagonal 				=> deny `+` (only able to put `x`) and `o` */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (o) : r = %u, c = %u \n", r, c);
				
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X, +)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X | DENY_P);
					continue;
				}
	
				/* row, column scan */
				if ((c == C) || (r == R))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (O, X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_X);
				}
			}
		}

		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (o) : r = %u, c = %u \n", r, c);

				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X, +)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X | DENY_P);
					continue;
				}

				/* diagonal scan */
				if (((r + c) == (R + C)) || ((r - c) == (R - C)))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (O, +)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_P);
				}
			}
		}


		break;
	
	case '+':
		pMdb->points += (1 - oldPoint);
	
		/* self[R][C]				=> deny `x` */
		/* diagonal 				=> deny `+` (only able to put `x`) */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (+) : r = %u, c = %u \n", r, c);
	
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X);							
					continue;
				}
	
			}
		}

		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (+) : r = %u, c = %u \n", r, c);

				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_X);							
					continue;
				}
				
				/* diagonal scan */
				if (((r + c) == (R + C)) || ((r - c) == (R - C)))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (+)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_P);
				}
			}
		}

		break;
	
	case 'x':
		pMdb->points += (1 - oldPoint);
		
		/* self[R][C]				=> deny `+` */
		/* row, column				=> deny `x` (only able to put `+`) and `o` */
	
		/* traverse */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf("{DBG} switch (x) : r = %u, c = %u \n", r, c);
				
				if ((r == R) && (c == C))
				{
					//printf("{DBG} self[%u][%u]=%c  -> DENY (+)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_P);							
					continue;
				}
	
				/* row, column scan */
				if ((c == C) || (r == R))
				{
					//printf("{DBG} RC[%u][%u]=%c  -> DENY (X)\n", r, c, MM[r][c]);
					pMdb->FF[r][c] |= (DENY_O | DENY_X);
				}
			}
		}
		break;
	
	default:
		break;
	}

	return 0;
}

#endif


int main(void) {
    uint32 T;

    scanf("%u\n", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
		struct mdb_s mdb;
		uint32 	i, r, c, d;	/* d = 1(left), 2(up), 3(right), 4(down) */
		uint32	N, M, R, C;
		char ch;

        /* Test Case run once */

		/* memory clear */
		memset(&mdb, 0x00, sizeof(mdb));
		memset(&mdb.MM, '.', sizeof(mdb.MM));
		memset(&mdb.PP, 0x00, sizeof(mdb.PP));

        scanf("%u %u\n", &N, &M);
		//printf("{DBG} N=%u, M=%u\n", N, M);

		mdb.N = N;
		mdb.M = M;
		mdb.points = 0;

		/* pre-placed */
		for (i=0; i<M; i++)
		{
			//printf("{DBG} (i, M) = (%u, %u)\n", i, M);
			scanf("%c %u %u\n", &ch, &R, &C);
			//printf("{DBG} %c %u %u\n", ch, R, C);
			
			traverse_mark_flags(&mdb, R, C, ch);
		}

		/* reset models here */
		mdb.models = 0;

#if 0
		/* (pre-placed) display for debugging */
		printf (" (pre-placed) display for debugging \n");
		printf ("------------------------------------\n");
		for (r=1; r<=N; r++)
		{
			for (c=1; c<=N; c++)
			{
				//printf("{DBG} switch (o) : r = %u, c = %u \n", r, c);
				printf("%c", mdb.MM[r][c]);
			}
			printf("\n");
		}
		printf ("------------------------------------\n");
		printf("points = %u, models = %u\n", mdb.points, mdb.models);
#endif

#if 0
		/* pre process (o only for 4 corners) */
		for (i=0; i<4; i++)
		{
			if (i==0)
			{
				r = N;
				c = N;
			}
			else if (i==1)
			{
				r = N;
				c = 1;
			}
			else if (i==2)
			{
				r = 1;
				c = N;
			}
			else if (i==3)
			{
				r = 1;
				c = 1;
			}

			//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);
			
			switch (mdb.MM[r][c])
			{
			case ' ':
				/* consider to put `o` ? */
				if (!(mdb.FF[r][c] & (DENY_O)))
				{
					//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
					traverse_mark_flags(&mdb, r, c, 'o');
				}
#if 0
				else if (!(mdb.FF[r][c] & (DENY_P)))
				{
					//printf("{DBG} <+> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], '+');
					traverse_mark_flags(&mdb, r, c, '+');
				}
				else if (!(mdb.FF[r][c] & (DENY_X)))
				{
					//printf("{DBG} <x> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'x');
					traverse_mark_flags(&mdb, r, c, 'x');
			
				}
#endif
				break;
			
				default:
					//printf("{DBG} SKIP RC[%u][%u]\n", rr, cc);
					break;
			}

		}
		
		for (i=0; i<4; i++)
		{
			if (i==0)
			{
				r = N;
				c = N;
			}
			else if (i==1)
			{
				r = N;
				c = 1;
			}
			else if (i==2)
			{
				r = 1;
				c = N;
			}
			else if (i==3)
			{
				r = 1;
				c = 1;
			}

			//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);
			
			switch (mdb.MM[r][c])
			{
			case 'o':
				break;
			
			case '+':
			case 'x':
				/* consider to put `o` ? */
				if (!(mdb.FF[r][c] & (DENY_O)))
				{
					//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
					traverse_mark_flags(&mdb, r, c, 'o');
				}
				break;
			
			case ' ':
				/* consider to put `o` ? */
				if (!(mdb.FF[r][c] & (DENY_O)))
				{
					//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
					traverse_mark_flags(&mdb, r, c, 'o');
				}
#if 0
				else if (!(mdb.FF[r][c] & (DENY_P)))
				{
					//printf("{DBG} <+> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], '+');
					traverse_mark_flags(&mdb, r, c, '+');
				}
				else if (!(mdb.FF[r][c] & (DENY_X)))
				{
					//printf("{DBG} <x> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'x');
					traverse_mark_flags(&mdb, r, c, 'x');
			
				}
#endif
				break;
			
				default:
					//printf("{DBG} SKIP RC[%u][%u]\n", rr, cc);
					break;
			}

		}
#endif

		/* main traverse */
#if 0 /* reference */
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);

				switch (mdb.MM[r][c])
				{
				case 'o':
					break;

				case '+':
				case 'x':
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');
					}
					break;

				case ' ':
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');

					}
					else if (!(mdb.FF[r][c] & (DENY_P)))
					{
						//printf("{DBG} <+> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], '+');
						traverse_mark_flags(&mdb, r, c, '+');
					}
					else if (!(mdb.FF[r][c] & (DENY_X)))
					{
						//printf("{DBG} <x> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'x');
						traverse_mark_flags(&mdb, r, c, 'x');
					}
					break;

					default:
						//printf("{DBG} SKIP RC[%u][%u]\n", rr, cc);
						break;
				}
			}
		}

		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);

				switch (mdb.MM[r][c])
				{
#if 0
				case 'o':
					break;
				
				case '+':
				case 'x':
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');
					}
					break;
#endif

				case ' ':
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');

					}
					break;

				default:
					//printf("{DBG} SKIP RC[%u][%u]\n", rr, cc);
					break;
				}
			}
		}
#endif

#if 0
		for (r=N; r>0; r--)
		{
			for (c=N; c>0; c--)
			{
				//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);

				switch (mdb.MM[r][c])
				{
				case 'o':
					break;

				case '+':
				case 'x':
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');
					}
					break;

				case '.':
				default:
					/* consider to put `o` ? */
					if (!(mdb.FF[r][c] & (DENY_O)))
					{
						//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
						traverse_mark_flags(&mdb, r, c, 'o');

					}
					else if (!(mdb.FF[r][c] & (DENY_P)))
					{
						//printf("{DBG} <+> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], '+');
						traverse_mark_flags(&mdb, r, c, '+');
					}
					else if (!(mdb.FF[r][c] & (DENY_X)))
					{
						//printf("{DBG} <x> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'x');
						traverse_mark_flags(&mdb, r, c, 'x');
					}
					break;
				}
			}
		}
#endif

		r = N;
		c = N;
		d = 1;

		while (true)
		{

			//printf ("{DBG} MAIN: RC[%u][%u] : 0x%02X, FF=0x%08X, points = %u, models = %u\n", rr, cc, MM[rr][cc], FF[rr][cc], points, models);

			switch (mdb.MM[r][c])
			{
			case 'o':
				break;

			case '+':
			case 'x':
				/* consider to put `o` ? */
				if (!(mdb.FF[r][c] & (DENY_O)))
				{
					//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
					traverse_mark_flags(&mdb, r, c, 'o');
				}
				break;

			case '.':
			default:
				/* consider to put `o` ? */
				if (!(mdb.FF[r][c] & (DENY_O)))
				{
					//printf("{DBG} <o> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'o');
					traverse_mark_flags(&mdb, r, c, 'o');

				}
				else if (!(mdb.FF[r][c] & (DENY_P)))
				{
					//printf("{DBG} <+> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], '+');
					traverse_mark_flags(&mdb, r, c, '+');
				}
				else if (!(mdb.FF[r][c] & (DENY_X)))
				{
					//printf("{DBG} <x> RC[%u][%u]: 0x%02X -> %c\n", rr, cc, MM[rr][cc], 'x');
					traverse_mark_flags(&mdb, r, c, 'x');
				}
				break;
			}

			/* move to the next */
			mdb.PP[r][c] = 1;
			switch (d)
			{
			case 1: /* left -> up -> right -> down */
				//printf ("{DBG} d == 1\n");
				if ((c > 1) && (mdb.PP[r][c-1] == 0))
				{
					c -= 1;
				}
				else if (( r > 1) && (mdb.PP[r-1][c] == 0))
				{
					d = 2;
					r -= 1;
				}
				else if ((c < N) && (mdb.PP[r][c+1] == 0))
				{
					d = 3;
					c += 1;
				}
				else if ((r < N) && (mdb.PP[r+1][c] == 0))
				{
					d = 4;
					r += 1;
				}
				else
				{
					d = 0;
					break;
				}
				break;

			case 2: /* up -> right -> down -> left */
				//printf ("{DBG} d == 2\n");
				if (( r > 1) && (mdb.PP[r-1][c] == 0))
				{
					r -= 1;
				}
				else if ((c < N) && (mdb.PP[r][c+1] == 0))
				{
					d = 3;
					c += 1;
				}
				else if ((r < N) && (mdb.PP[r+1][c] == 0))
				{
					d = 4;
					r += 1;
				}
				else if ((c > 1) && (mdb.PP[r][c-1] == 0))
				{
					d = 1;
					c -= 1;
				}
				else
				{
					d = 0;
					break;
				}
				break;

			case 3: /* right -> down -> left -> up */
				//printf ("{DBG} d == 3\n");
				if ((c < N) && (mdb.PP[r][c+1] == 0))
				{
					c += 1;
				}
				else if ((r < N) && (mdb.PP[r+1][c] == 0))
				{
					d = 4;
					r += 1;
				}
				else if ((c > 1) && (mdb.PP[r][c-1] == 0))
				{
					d = 1;
					c -= 1;
				}
				else if (( r > 1) && (mdb.PP[r-1][c] == 0))
				{
					d = 2;
					r -= 1;
				}
				else 
				{
					d = 0;
					break;
				}
				break;

			case 4: /* down -> left -> up -> right */
				//printf ("{DBG} d == 4\n");
				if ((r < N) && (mdb.PP[r+1][c] == 0))
				{
					r += 1;
				}
				else if ((c > 1) && (mdb.PP[r][c-1] == 0))
				{
					d = 1;
					c -= 1;
				}
				else if (( r > 1) && (mdb.PP[r-1][c] == 0))
				{
					d = 2;
					r -= 1;
				}
				else if ((c < N) && (mdb.PP[r][c+1] == 0))
				{
					d = 3;
					c += 1;
				}
				else 
				{
					d = 0;
					break;
				}
				break;

			default:
				d = 0;
				break;
			}


			if (d == 0)
				break;

			//printf ("{DBG} r = %u, c = %u\n", r, c);
		}


#if 0
		/* display for debugging */
		printf ("----------\n");
		for (r=1; r<=N; r++)
		{
			for (c=1; c<=N; c++)
			{
				//printf("{DBG} switch (o) : r = %u, c = %u \n", r, c);
				printf("%1c", mdb.MM[r][c]);
			}
			printf("\n");
		}
#endif


        /* Print */
    	printf("Case #%d: %u %u\n", Ti, mdb.points, mdb.models);
		for (i=0; i<mdb.models; i++)
		{
			printf("%1c %u %u\n", mdb.as[i], mdb.ar[i], mdb.ac[i]);
		}
    }

    return 0;
}

