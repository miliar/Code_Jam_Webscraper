#include <fstream>

using namespace std;

int N;//, R, O, Y, G, B, V;
int num[6];
char result[1001];
char priority[7];
char base_priority[7][7];

bool colide(char now, char last) {
	switch (now) {
	case 'R':
		if (last == 'O' || last == 'V' || last == now)
			return true;
		else
			return false;
		break;
	case 'O':
		if (last == 'R' || last == 'Y' || last == now)
			return true;
		else
			return false;
		break;
	case 'Y':
		if (last == 'O' || last == 'G' || last == now)
			return true;
		else
			return false;
		break;
	case 'G':
		if (last == 'Y' || last == 'B' || last == now)
			return true;
		else
			return false;
		break;
	case 'B':
		if (last == 'G' || last == 'V' || last == now)
			return true;
		else
			return false;
		break;
	case 'V':
		if (last == 'R' || last == 'B' || last == now)
			return true;
		else
			return false;
		break;
	}
}

char num_to_char(int num) {
	switch (num) {
	case 0:
		return 'R';
		break;
	case 1:
		return 'B';
		break;
	case 2:
		return 'Y';
		break;
	case 3:
		return 'O';
		break;
	case 4:
		return 'G';
		break;
	case 5:
		return 'V';
		break;
	default:
		return 'I';
		break;
	}
}

int char_to_num(char a) {
	switch (a) {
	case 'R':
		return 0;
		break;
	case 'B':
		return 1;
		break;
	case 'Y':
		return 2;
		break;
	case 'O':
		return 3;
		break;
	case 'G':
		return 4;
		break;
	case 'V':
		return 5;
		break;
	case 'I':
		return 6;
		break;
	}
}

void remove_from_priority(char a) {
	int len = strlen(priority);

	bool found = false;
	for (int i = 0; i < len; i++) {
		if (found || priority[i] == a) {
			found = true;
			priority[i] = priority[i + 1];
		}
	}
}

char decide_first(char last) {
	bool isMax[6];
	int max = 0;
	for (int i = 0; i < 6; i++) {
		if (max < num[i] && num[i] > 0 && !colide(num_to_char(i), last))
			max = num[i];
	}

	for (int i = 0; i < 6; i++) {
		if (num[i] == max && num[i] > 0)
			isMax[i] = true;
		else
			isMax[i] = false;
	}

	for (int i = 0; i < 6; i++) {
		if (isMax[i] == false)
			remove_from_priority(num_to_char(i));
	}
}

bool is_in_priority(char a) {
	int len = strlen(priority);

	for (int i = 0; i < len; i++) {
		if (priority[i] == a) {
			return true;
		}
	}
	return false;
}
/*
char decide(char first, char last) {
	int start = char_to_num(first);
	for (int i = 0; i < 7; i++) {
		priority[i] = base_priority[start][i];
	}
	
	decide_first(last);
	bool isMax[6];
	int group[6];
	group[0] = num[0] + num[3] + num[5]; // R
	group[1] = num[1] + num[5] + num[4]; // B
	group[2] = num[2] + num[3] + num[4]; // Y
	group[3] = group[0] + group[2]; // O
	group[4] = group[2] + group[1]; // G
	group[5] = group[0] + group[1]; // V
	
	int max = 0;
	for (int i = 0; i < 6; i++) {
		if (max < group[i] && num[i] > 0 && is_in_priority(num_to_char(i)))
			max = group[i];
	}

	for (int i = 0; i < 6; i++) {
		if (group[i] == max && num[i] > 0)
			isMax[i] = true;
		else
			isMax[i] = false;
	}

	char now;
	for(int i = 0; i < 6; i++) {
		now = priority[i];
		switch (now) {
		case 'R':
			if (isMax[0] && !colide(now, last) && num[0] > 0) {
				num[0]--;
				return 'R';
			}
			break;
		case 'B':
			if (isMax[1] && !colide(now, last) && num[1] > 0) {
				num[1]--;
				return 'B';
			}
			break;
		case 'Y':
			if (isMax[2] && !colide(now, last) && num[2] > 0) {
				num[2]--;
				return 'Y';
			}
				break;
		case 'O':
			if (isMax[3] && !colide(now, last) && num[3] > 0) {
				num[3]--;
				return 'O';
			}
				break;
		case 'G':
			if (isMax[4] && !colide(now, last) && num[4] > 0) {
				num[4]--;
				return 'G';
			}
				break;
		case 'V':
			if (isMax[5] && !colide(now, last) && num[5] > 0) {
				num[5]--;
				return 'V';
			}
				break;
		}
	}
	return 'I';
}
*/

char decide(char first, char last) {
	int start = char_to_num(first);
	for (int i = 0; i < 7; i++) {
		priority[i] = base_priority[start][i];
	}

	decide_first(last);
	
	char now;
	for (int i = 0; i < 6; i++) {
		now = priority[i];
		switch (now) {
		case 'R':
			if (!colide(now, last) && num[0] > 0) {
				num[0]--;
				return 'R';
			}
			break;
		case 'B':
			if (!colide(now, last) && num[1] > 0) {
				num[1]--;
				return 'B';
			}
			break;
		case 'Y':
			if (!colide(now, last) && num[2] > 0) {
				num[2]--;
				return 'Y';
			}
			break;
		case 'O':
			if (!colide(now, last) && num[3] > 0) {
				num[3]--;
				return 'O';
			}
			break;
		case 'G':
			if (!colide(now, last) && num[4] > 0) {
				num[4]--;
				return 'G';
			}
			break;
		case 'V':
			if (!colide(now, last) && num[5] > 0) {
				num[5]--;
				return 'V';
			}
			break;
		}
	}
	return 'I';
}

void run() {
	char ret;
	for (int i = 0; i < N; i++) {
		if (i == 0) {
			ret = decide('I', 'I');
		}
		else {
			ret = decide(result[0], result[i-1]);
		}
		
		if (ret == 'I') {
			strcpy_s(result, "IMPOSSIBLE");
			return;
		}
		else {
			result[i] = ret;
		}
	}
	
	if (colide(result[0], result[N - 1])) {
		strcpy_s(result, "IMPOSSIBLE");
		return;
	}
	result[N] = '\0';
}

int main() {
	strcpy_s(base_priority[0] ,"OVGRBY");//R
	strcpy_s(base_priority[1], "GVOBYR");//B
	strcpy_s(base_priority[2], "OGVYRB");//Y
	strcpy_s(base_priority[3], "OVGRYB");//O
	strcpy_s(base_priority[4], "GOVYBR");//G
	strcpy_s(base_priority[5], "VOGRBY");//V
	strcpy_s(base_priority[6], "GOVBYR");//I
	int T;
	ifstream in("B-small-attempt0.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		//read file
		in >> N >> num[0] >> num[3] >> num[2] >> num[4] >> num[1] >> num[5];
		//run
		run();
		//output
		out << "Case #" << t + 1 << ": " << result << endl;
	}
	in.close();
	out.close();
	return 0;
}