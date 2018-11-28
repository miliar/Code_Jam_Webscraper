#include <stdio.h>
#include <vector>
#include <cassert>

using namespace std;

// R = 1
// Y = 2
// B = 4
// O = R + Y = 3
// G = Y + B = 6
// V = R + B = 5

vector<int> make_pillow(int n21, int v2, int v1) {
	vector<int> v;
	v.push_back(v1);
	for (int i = 0; i < n21; i++) {
		v.push_back(v2);
		v.push_back(v1);
	}
	return v;
}

void put(vector<pair<int, int>> &p_cnt_n, int idx, vector<int> &ret) {
	ret.push_back(1 << p_cnt_n[idx].second);
	p_cnt_n[idx].first--;
}

vector<int> handle_complex(int n001, int n010, int n100, int n011, int n101, int n110) {
	vector<int> fail;

	vector<int> p011;
	if (n011 > 0) {
		if (n100 < n011 + 1)
			return fail;
		p011 = make_pillow(n011, 3, 4);
		n100 -= n011 + 1;
	}

	vector<int> p101;
	if (n101 > 0) {
		if (n010 < n101 + 1)
			return fail;
		p101 = make_pillow(n101, 5, 2);
		n010 -= n101 + 1;
	}

	vector<int> p110;
	if (n110 > 0) {
		if (n001 < n110 + 1)
			return fail;
		p110 = make_pillow(n110, 6, 1);
		n001 -= n110 + 1;
	}

	vector<pair<int, int>> p_cnt_n;
	p_cnt_n.push_back(make_pair(n001, 0));
	p_cnt_n.push_back(make_pair(n010, 1));
	p_cnt_n.push_back(make_pair(n100, 2));
	sort(p_cnt_n.begin(), p_cnt_n.end());
	if (p_cnt_n[2].first > p_cnt_n[1].first + p_cnt_n[0].first + 1)
		return fail;

	//printf("n100 %d %d %d\n", p_cnt_n[2].first, p_cnt_n[1].first, p_cnt_n[0].first);
	vector<int> major_seg;
	put(p_cnt_n, 2, major_seg);
	while (p_cnt_n[2].first > 0) {
		if (p_cnt_n[2].first <= p_cnt_n[1].first && p_cnt_n[2].first <= p_cnt_n[0].first) {
	//printf("n100a\n");
			put(p_cnt_n, 0, major_seg);
			put(p_cnt_n, 1, major_seg);
			put(p_cnt_n, 2, major_seg);
	//printf("n100a\n");
		}
		else {
	//printf("n100b\n");
			if (p_cnt_n[1].first > p_cnt_n[0].first) {
				put(p_cnt_n, 1, major_seg);
				put(p_cnt_n, 2, major_seg);
			}
			else {
				put(p_cnt_n, 0, major_seg);
				put(p_cnt_n, 2, major_seg);
			}
	//printf("n100b\n");
		}
	}

	assert(p_cnt_n[1].first == 0 || p_cnt_n[1].first == 1);
	assert(p_cnt_n[0].first == 0 || p_cnt_n[0].first == 1);

	vector<int> b101, b011, b110;
	vector<int>* arr[3] = {&b110, &b101, &b011};

	//printf("n200 %d\n", p_cnt_n[2].second);
	*arr[ p_cnt_n[2].second ] = major_seg;
	for (int i = 1; i >= 0; i--) {
		//printf("xx %d %d\n", p_cnt_n[i].first, p_cnt_n[i].second);
		if (p_cnt_n[i].first == 1)
			arr[ p_cnt_n[i].second ]->push_back(1 << p_cnt_n[i].second);
	}

	//printf("n200\n");
	vector<int> ret;
	ret.insert( ret.end(), p011.begin(), p011.end() );
	//ret.push_back(7);
	ret.insert( ret.end(), b110.begin(), b110.end() );
	//ret.push_back(7);
	ret.insert( ret.end(), p101.begin(), p101.end() );
	//ret.push_back(7);
	ret.insert( ret.end(), b011.begin(), b011.end() );
	//ret.push_back(7);
	ret.insert( ret.end(), p110.begin(), p110.end() );
	//ret.push_back(7);
	ret.insert( ret.end(), b101.begin(), b101.end() );
	//ret.push_back(7);
	//printf("n200\n");
	return ret;
}


vector<int> handle_single(int n001, int n010, int n100) {
	vector<int> fail;

	vector<pair<int, int>> p_cnt_n;
	p_cnt_n.push_back(make_pair(n001, 0));
	p_cnt_n.push_back(make_pair(n010, 1));
	p_cnt_n.push_back(make_pair(n100, 2));
	sort(p_cnt_n.begin(), p_cnt_n.end());
	if (p_cnt_n[2].first > p_cnt_n[1].first + p_cnt_n[0].first)
		return fail;

	vector<int> major_seg;
	while (p_cnt_n[2].first > 0) {
		if (p_cnt_n[2].first == p_cnt_n[1].first && p_cnt_n[2].first == p_cnt_n[0].first) {
			put(p_cnt_n, 2, major_seg);
			put(p_cnt_n, 1, major_seg);
			put(p_cnt_n, 0, major_seg);
		}
		else {
			if (p_cnt_n[1].first > p_cnt_n[0].first) {
				put(p_cnt_n, 2, major_seg);
				put(p_cnt_n, 1, major_seg);
			}
			else {
				put(p_cnt_n, 2, major_seg);
				put(p_cnt_n, 0, major_seg);
			}
		}
	}

	return major_seg;
}

vector<int> handle_pair(int n1, int n2, int v1, int v2) {
	//printf("pair, %d %d %d %d\n", n1, n2, v1, v2);
	vector<int> fail;
	if (n1 != n2)
		return fail;
	
	vector<int> ret;
	for (int i = 0; i < n1; i++) {
		ret.push_back(v1);
		ret.push_back(v2);
	}
	return ret;
}

vector<int> handle(int n001, int n010, int n100, int n011, int n101, int n110, int en) {
	if (n011 == 0 && n101 == 0 && n110 == 0)
		return handle_single(n001, n010, n100);
	else if (n001 + n110 == en)
		return handle_pair(n001, n110, 1, 6);
	else if (n010 + n101 == en)
		return handle_pair(n010, n101, 2, 5);
	else if (n100 + n011 == en)
		return handle_pair(n100, n011, 4, 3);
	else
		return handle_complex(n001, n010, n100, n011, n101, n110);
}

int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	if (argc > 1) {
		if (sscanf(argv[1], "%d", &caseStart) == 1) {
			if (argc > 2)
				sscanf(argv[2], "%d", &caseEnd);
		}
		if (caseEnd < caseStart)
			caseEnd = caseStart;
		if (caseEnd != 9999999 && caseEnd >= 1 && caseStart <= 0)
			caseStart = 1;
		if (caseStart > 0)
			fprintf(stderr, "....................DEBUG MODE ENABLED (FROM CASE %d to %d)\n", caseStart, caseEnd);
	}


	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		// R = 1
		// Y = 2
		// B = 4
		// O = R + Y = 3
		// G = Y + B = 6
		// V = R + B = 5
		
		//      R     Y     B     G     V     O
		int en, n001, n010, n100, n110, n101, n011;
		//       R O Y G B V      
		scanf("%d%d%d%d%d%d%d", &en, &n001, &n011, &n010, &n110, &n100, &n101);

		vector<int> result = handle(n001, n010, n100, n011, n101, n110, en);
		printf("Case #%d: ", ecount);
		if (result.size() == 0)
			printf("IMPOSSIBLE");
		else {
			char printable[10] = ".RYOBVG-";
			for (int n : result)
				printf("%c", printable[n]);
		}
		printf("\n");
		
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
