#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#define all(a) a.begin(), a.end()

using namespace std;

typedef unsigned long long int llu;
typedef map< llu, llu > MII;
typedef vector< llu > VI;
typedef vector<VI> VVI;
typedef set< llu > SI;
typedef pair <llu, llu> PII;
typedef vector < PII > VPII;


#define DEBUG

#ifdef DEBUG
    #define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)
    void DE_MII(MII &m) {
        for (MII::iterator mit = m.begin(); mit != m.end(); ++mit)
            DE(" %llu:%llu", mit->first, mit->second);
        DE("\n");
    }

    void DE_VI(VI &v) {
        for (size_t i=0; i < v.size(); ++i) {
            DE(" %llu", v[i]);
        }
        DE("\n");
    }
    void DE_VPII(VPII &v) {
        for (size_t i=0; i < v.size(); ++i) {
            PII p = v[i];
            DE(" %llu->%llu", p.first, p.second);
        }
        DE("\n");
    }

    #define DI for(int i=0;i<indent;i++) DE("  ");
#else
    #define DI
    #define DE(format, ...)
    #define DE_MII(m)
    #define DE_VI(v)
#endif


void solve()
{
	llu N, R, RY, Y, YB, B, BR;
    VPII num2color;
	scanf("%llu", &N);
    for (int i = 0; i < 6; i++)
    {
        llu num;
        scanf("%llu", &num);
        num2color.push_back(PII(num, i));
    }
    sort (num2color.begin(), num2color.end());
    reverse (num2color.begin(), num2color.end());
    DE("Num2color: "); DE_VPII(num2color);

    vector<char> idx2color = {'R','O', 'Y', 'G', 'B', 'V'};
    int size = idx2color.size();
    VI result;

    for (int i = 0; i < N; i++) {
        DE("Current: "); DE_VPII(num2color);
        int max_color_idx = -1;
        for (int cidx = 0; cidx < num2color.size(); cidx++)
        {
            int num = num2color[cidx].first;
            int color = num2color[cidx].second;
            if (0 == num) {
                continue;
            }
          
            if (!result.empty()) {
                int prev_color = result.back();
                //DE("prev_color, color = %llu %llu\n", prev_color, color);
                if (prev_color == color ||
                (size + color - prev_color) % size == 1 ||
                (size + color - prev_color) % size == size - 1) {
                    //DE("Colors %llu %llu - skipping\n", prev_color, color);
                    continue;
                }
            }
            if (-1 == max_color_idx  || num > num2color[max_color_idx].first) {
                max_color_idx = cidx;
            }
        }

        if (-1 == max_color_idx) {
            fprintf(stderr, "Impossible1\n");
            printf("IMPOSSIBLE\n");
            return;
        }
        result.push_back(num2color[max_color_idx].second);
        --(num2color[max_color_idx].first);
        //DE("Result: "); DE_VI(result);
    }
    
    if (result[0] == result.back())
    {
        fprintf(stderr, "Impossible2\n");
        printf("IMPOSSIBLE\n");
        return;
    }

    fprintf(stderr, "Result: ");
    for(int i = 0; i < result.size(); i++) {
        fprintf(stderr, "%c", idx2color[result[i]]);
        printf("%c", idx2color[result[i]]);
    }
    fprintf(stderr, "\n");
    printf("\n");
	
	//fprintf(stderr, "!!!!result = %llu\n\n", result);
	//printf("%llu\n", result);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		fprintf(stderr, "Debug Case #%d:\n", i);
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
