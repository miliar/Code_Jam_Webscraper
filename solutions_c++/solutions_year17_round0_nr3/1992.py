
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <Windows.h>
#include <algorithm>
#include <utility> 
#include <assert.h>

using namespace std;

CRITICAL_SECTION		CS;

enum TASK_STATE
{
	TASK_ADDED,
	TASK_PROCESSING,
	TASK_COMPLETED,
};

struct Task
{
	int						case_number;
	int						state;
	string					result;
	int						time;

	long long				N;
	long long				K;

	Task					() : case_number(-1), state(TASK_ADDED) {}
};

vector<Task>				tasks;

void update_stalls(map<long long, long long>& stalls, long long val, long long count = 1)
{
	auto it = stalls.find(val);
	if (it == stalls.end()) {
		stalls[val] = count;
	} else {
		it->second += count;
	}
}

pair<long long, long long> brut_force(Task& t)
{
	long long n = t.N;
	long long k = t.K;
	map<long long, long long> stalls;
	stalls[n] = 1;
	while (k > 1) {
		auto it = stalls.end();
		--it;
		if (it->first == 1) {
			it->second--;
		} else {
			long long x = it->first;
			it->second--;
			if (it->second == 0) {
				stalls.erase(it);
			}
			long long y = (x - 1) - (x - 1) / 2;
			x = (x - 1) / 2;

			update_stalls(stalls, x);
			update_stalls(stalls, y);
		}
		--k;
	}
	long long x = stalls.rbegin()->first;
	long long l_max = (x - 1) - (x - 1) / 2;
	long long l_min = (x - 1) / 2;
	return make_pair(l_max, l_min);
}

pair<long long, long long> execute(Task& t)
{
	long long n = t.N;
	long long k = t.K;
	map<long long, long long> stalls;
	stalls[n] = 1;
	while (k > 1) {
		auto it = stalls.end();
		--it;
		if (it->first == 1) {
			return make_pair(0, 0);
		}
		long long x = it->first;
		long long count = (k > it->second) ? it->second : k - 1;
		it->second -= count;
		if (it->second == 0) {
			stalls.erase(it);
		}
		long long y = (x - 1) - (x - 1) / 2;
		x = (x - 1) / 2;

		update_stalls(stalls, x, count);
		update_stalls(stalls, y, count);
		k -= count;
	}
	long long x = stalls.rbegin()->first;
	long long l_max = (x - 1) - (x - 1) / 2;
	long long l_min = (x - 1) / 2;
	return make_pair(l_max, l_min);
}

void execute_task			(Task& t)
{
	pair<long long, long long> result = execute(t);
	//pair<long long, long long> check_result = brut_force(t);
	//if (result != check_result) {
	//	MessageBox(nullptr, TEXT("Assert!!"), TEXT("Message"), MB_OK);
	//	exit(1);
	//}
	//assert(result == check_result);
	stringstream ss;
	ss << result.first << " " << result.second;
	t.result				= ss.str();
}

bool get_line				(ifstream& stream, char* buffer, int buffer_size)
{
	if (!stream.good()) {
		cout << "wrong input file format" << endl;
		return false;
	}
	stream.getline			(buffer, buffer_size);
	return true;
}

bool read_task				(Task& t, ifstream& file)
{
	char buffer[4*4096];
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss		(buffer);
		ss >> t.N;
		ss >> t.K;
	}
	//t.lawn.resize			(t.Cols);
	//for (int i=0; i<t.Cols; ++i) {
	//	t.lawn[i].resize	(t.Rows);
	//}
	//for (int r=0; r<t.Rows; ++r) {
	//	if (!get_line(file, buffer, sizeof(buffer))) {
	//		return false;
	//	}
	//	stringstream ss		(buffer);
	//	for (int c=0; c<t.Cols; ++c) {
	//		ss >> t.lawn[c][r];
	//	}
	//}

	return true;
}

void print_task				(Task& t)
{
	//cout << "Task #" << t.case_number << " Text = " << t.N << endl;
}

void print_result			(Task& t)
{
	cout << "Case #" << t.case_number << ": " << t.result.c_str() << endl;
}

DWORD WINAPI worker_thread	(void* arg)
{
	while (true) {
		Task* t				= 0;
		{
			EnterCriticalSection(&CS);
			for (int i=0, size=tasks.size(); i!=size; ++i) {
				if (tasks[i].state == 0) {
					t		= &tasks[i];
					t->state= TASK_PROCESSING;
					break;
				}
			}
			LeaveCriticalSection(&CS);
		}
		if (t == 0) {
			return 0;
		}
		execute_task		(*t);
		t->state			= TASK_COMPLETED;
	}
	return 0;
}

int main					(int argc, char** argv)
{
	if (argc < 2) {
		cout << "Input file missing" << endl;
		return -1;
	}
	int time				= timeGetTime();
	ifstream file			(argv[1]);
	if (!file.is_open()) {
		return -1;
	}
	char line[4*4096];
	file.getline			(line, sizeof(line));
	int line_count			= atoi(line);
	tasks.resize			(line_count);
	for (int i=0; i!=line_count; ++i) {
		Task& t = tasks[i];
		t.case_number = i + 1;
		if (!read_task(t, file)) {
			return -1;
		}
	}

	if (IsDebuggerPresent()) {
		for (int i=0; i!=tasks.size(); ++i) {
			Task& t			= tasks[i];
			t.time			= timeGetTime();
			//print_task	(t);
			execute_task	(t);
			t.time			= timeGetTime() - t.time;
			//cout << "Task " << t.case_number << " done in [" << t.time << "] ms" << endl;
			print_result	(t);
		}
	} else {
		InitializeCriticalSection(&CS);
		HANDLE handles[4];
		for (int i=0; i<4; ++i) {
			handles[i]			= CreateThread( NULL, 0, &worker_thread, 0, 0, 0);
		}
		WaitForSingleObject		(handles[0], INFINITE);
		WaitForSingleObject		(handles[1], INFINITE);
		WaitForSingleObject		(handles[2], INFINITE);
		WaitForSingleObject		(handles[3], INFINITE);
		DeleteCriticalSection	(&CS);

		//cout << "Work done in [" << timeGetTime() - time << "] ms" << endl;
		for (int i=0; i!=tasks.size(); ++i) {
			print_result		(tasks[i]);
		}
	}
	return 0;
}
