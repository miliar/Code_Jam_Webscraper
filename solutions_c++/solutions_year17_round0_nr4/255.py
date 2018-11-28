#include <ios>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

bool row[505] = {};
bool col[505] = {};
bool ld[505] = {};
bool rd[505] = {};
std::vector<std::vector<int> > adjlist;
std::vector<int> visit;
std::vector<int> match;
std::vector<std::pair<int, int> > ans_rc;
std::vector<std::pair<int, int> > ans_d;
std::vector<std::pair<int, int> > ans_req;
std::vector<std::pair<char, std::pair<int, int> > > final_ans;

int aug(int a)
{
	int b;
	if (visit[a]) return 0;
	visit[a] = 1;
	for (int i = 0; i < adjlist[a].size(); i++)
	{
		b = adjlist[a][i];
		if (match[b] == -1 || aug(match[b]))
		{
			match[b] = a;
			return 1;
		}
	}
	return 0;
}

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //std::ios_base::sync_with_stdio(false);
    //std::cin.tie(NULL);
    //std::cout.tie(NULL);
    int tc, x, y, n, k, mcbm, final_beauty;
    char c;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        std::cout << "Case #" << t+1 << ": ";
        ans_req.clear();
        ans_rc.clear();
        ans_d.clear();
        final_ans.clear();
        final_beauty = 0;
        std::cin >> n >> k;
        for (int i = 0; i < n; i++)
        {
            row[i] = true;
            col[i] = true;
        }
        for (int i = 0; i < 2*n-1; i++)
        {
            ld[i] = true;
            rd[i] = true;
        }
        for (int i = 0; i < k; i++)
        {
            std::cin >> c >> x >> y;
            x--; y--;
            ans_req.push_back(std::make_pair(x, y));
            if (c == 'x') //hurts a row and column
            {
                final_beauty++;
                row[x] = false;
                col[y] = false;
            }
            if (c == '+') //hurts a ld and rd
            {
                final_beauty++;
                ld[x+y] = false;
                rd[n+x-y-1] = false;
            }
            if (c == 'o') //hurts like both + and x
            {
                final_beauty+=2;
                row[x] = false;
                col[y] = false;
                ld[x+y] = false;
                rd[n+x-y-1] = false;
            }
        }
        adjlist.clear();
        adjlist.resize(2*n);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (row[i] && col[j])
                    adjlist[i].push_back(n+j);
            }
        }

        //ROWS AND COLUMNS

        mcbm = 0;
        match.assign(2*n, -1);
        for (int i = 0; i < n; i++)
        {
        	visit.assign(n, 0);
        	mcbm += aug(i);
        }
        final_beauty += mcbm;
        for (int i = n; i < 2*n; i++)
        {
            if (match[i] != -1)
                ans_rc.push_back(std::make_pair(match[i], i-n));
        }

        //DIAGONALS

        adjlist.clear();
        adjlist.resize(4*n-2);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (ld[i+j] && rd[n+i-j-1])
                    adjlist[i+j].push_back(2*n-1+n+i-j-1);
            }
        }
        mcbm = 0;
        match.assign(4*n-2, -1);
        for (int i = 0; i < 2*n-1; i++)
        {
        	visit.assign(2*n-1, 0);
        	mcbm += aug(i);
        }
        final_beauty += mcbm;
        for (int i = 2*n-1; i < 4*n-2; i++)
        {
            if (match[i] != -1)
            {
                int cld = match[i];
                int crd = i-(2*n-1);
                ans_d.push_back(std::make_pair((cld+crd-n+1)/2, (cld-crd+n-1)/2));
            }
        }
        std::sort(ans_rc.begin(), ans_rc.end());
        std::sort(ans_d.begin(), ans_d.end());
        std::sort(ans_req.begin(), ans_req.end());

        for (std::vector<std::pair<int, int> >::iterator it = ans_rc.begin(); it != ans_rc.end(); it++)
        {
            if (std::binary_search(ans_d.begin(), ans_d.end(), std::make_pair(it->first, it->second)))
                final_ans.push_back(std::make_pair('o', std::make_pair(it->first+1, it->second+1)));
            else if (std::binary_search(ans_req.begin(), ans_req.end(), std::make_pair(it->first, it->second)))
                final_ans.push_back(std::make_pair('o', std::make_pair(it->first+1, it->second+1)));
            else
                final_ans.push_back(std::make_pair('x', std::make_pair(it->first+1, it->second+1)));
        }
        for (std::vector<std::pair<int, int> >::iterator it = ans_d.begin(); it != ans_d.end(); it++)
        {
            if (std::binary_search(ans_rc.begin(), ans_rc.end(), std::make_pair(it->first, it->second)));
            else if (std::binary_search(ans_req.begin(), ans_req.end(), std::make_pair(it->first, it->second)))
                final_ans.push_back(std::make_pair('o', std::make_pair(it->first+1, it->second+1)));
            else
                final_ans.push_back(std::make_pair('+', std::make_pair(it->first+1, it->second+1)));
        }
        std::cout << final_beauty << ' ' << final_ans.size() << '\n';
        for (std::vector<std::pair<char, std::pair<int, int> > >::iterator it = final_ans.begin(); it != final_ans.end(); it++)
        {
            std::cout << it->first << ' ' << it->second.first << ' ' << it->second.second << '\n';
        }
    }
}
