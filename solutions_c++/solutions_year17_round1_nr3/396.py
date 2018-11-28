#include <iostream>
#include <queue>
#include <cstring>

struct pos
{
	pos(){}
	pos(int a, int b, int c, int d)
	{
		hd = a;
		ad = b;
		hk = c;
		ak = d;
	}
	int hd, ad, hk, ak;
};

int dist[101][101][101][101];

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		int hd, ad, hk, ak;
		std::cin >> hd >> ad >> hk >> ak;
		memset(dist, 0x3f, sizeof dist);
		//std::cout << "debug\n";
		std::queue<pos> q;
		q.push(pos(hd, ad, hk, ak));
		int ans = 0x3f3f3f3f;
		dist[hd][ad][hk][ak] = 0;
		int b, d;
		std::cin >> b >> d;
		while(!q.empty())
		{
			pos cur = q.front();
			//std::cout << "on (" << cur.hd << ", " << cur.ad << ", " << cur.hk << ", " << cur.ak << ")\n";
			int cur_dist = dist[cur.hd][cur.ad][cur.hk][cur.ak];
			q.pop();
			pos nxt;

			nxt = cur;
			nxt.ak = std::max(0, nxt.ak - d);
			nxt.hd -= nxt.ak;
			if(nxt.hd > 0)
			{
				if(dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] > cur_dist + 1)
				{
					dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] = cur_dist + 1;
					q.push(nxt);
				}
			}

			nxt = cur;
			nxt.ad += b;
			nxt.hd -= nxt.ak;
			if(nxt.hd > 0)
			{
				if(dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] > cur_dist + 1)
				{
					dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] = cur_dist + 1;
					q.push(nxt);
				}
			}

			nxt = cur;
			nxt.hd = hd;
			nxt.hd -= nxt.ak;
			if(nxt.hd > 0)
			{
				if(dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] > cur_dist + 1)
				{
					dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] = cur_dist + 1;
					q.push(nxt);
				}
			}

			nxt = cur;
			nxt.hk -= nxt.ad;
			if(nxt.hk <= 0)
			{
				ans = cur_dist + 1;
				break;
			}
			nxt.hd -= nxt.ak;
			if(nxt.hd > 0)
			{
				if(dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] > cur_dist + 1)
				{
					dist[nxt.hd][nxt.ad][nxt.hk][nxt.ak] = cur_dist + 1;
					q.push(nxt);
				}
			}
		}
		std::cout << "Case #" << te << ": ";
		if(ans != 0x3f3f3f3f)
			std::cout << ans << '\n';
		else
			std::cout << "IMPOSSIBLE\n";
	}
}