#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using std::ifstream;
using std::vector;
using std::max;
using std::min;

const long long INPUT_MIN_VALUE = 0;
const long long INPUT_MAX_VALUE = 100000;

const long long INPUT_MAX_NET_NODE_SUM = 10000;
const long long INPUT_MAX_CONSUMER_NODE_SUM = 10000;

const long long INPUT_MAX_LINK_SUM = min(INPUT_MAX_NET_NODE_SUM * INPUT_MAX_NET_NODE_SUM, INPUT_MAX_VALUE);
const long long INPUT_MAX_LINK_SUM_PER_NODE = 10000;

const long long INPUT_MIN_LINK_BANDWIDTH = max(0LL, INPUT_MIN_VALUE);
const long long INPUT_MAX_LINK_BANDWIDTH = min(100LL, INPUT_MAX_VALUE);
const long long INPUT_MIN_COST_PER_LINK_BANDWIDTH = max(0LL, INPUT_MIN_VALUE);
const long long INPUT_MAX_COST_PER_LINK_BANDWIDTH = min(100LL, INPUT_MAX_VALUE);

const long long INPUT_MIN_CLASS_SUM = 1;
const long long INPUT_MAX_CLASS_SUM = 10;

const long long INPUT_MIN_SERVER_OUTPUT_ABILITY = max(0LL, INPUT_MIN_VALUE);
const long long INPUT_MAX_SERVER_OUTPUT_ABILITY = min(10000LL, INPUT_MAX_VALUE);

const long long INPUT_MIN_SERVER_HARDWARE_COST = INPUT_MIN_VALUE;
const long long INPUT_MAX_SERVER_HARDWARE_COST = INPUT_MAX_VALUE;

const long long INPUT_MIN_SERVER_DEPLOY_COST = max(0LL, INPUT_MIN_VALUE);
const long long INPUT_MAX_SERVER_DEPLOY_COST = min(10000LL, INPUT_MAX_VALUE);

const long long INPUT_MIN_CONSUMER_REQUIRE_BANDWIDTH = max(0LL, INPUT_MIN_VALUE);
const long long INPUT_MAX_CONSUMER_REQUIRE_BANDWIDTH = min(5000LL, INPUT_MAX_VALUE);

const long long OUTPUT_MIN_VALUE = 0;
const long long OUTPUT_MAX_VALUE = 1000000;

const long long OUTPUT_MIN_ROUTE_SUM = max(0LL, OUTPUT_MIN_VALUE);
const long long OUTPUT_MAX_ROUTE_SUM = min(300000LL, OUTPUT_MAX_VALUE);

const long long OUTPUT_MIN_NODE_SUM_PER_ROUTE = 0;
const long long OUTPUT_MAX_NODE_SUM_PER_ROUTE = 10000;

//const long long OUTPUT_MIN_CLASS_NUM = max(INPUT_MIN_CLASS_SUM-1, OUTPUT_MIN_VALUE);
//const long long OUTPUT_MAX_CLASS_NUM = min(INPUT_MAX_CLASS_SUM-1, OUTPUT_MAX_VALUE);


bool check_fp(FILE *fp) {
    return fp != NULL;
}

bool in(long long value, long long min_value, long long max_value) {
    if (max_value == 0 || max_value <= min_value) {
        printf("Warning: min_value is %lld, max_value is %lld\n", min_value, max_value);
    }
    return value >= min_value && value <= max_value;
}

bool check_input_net_node_sum(long long node_num) {
    return in(node_num, max(0LL, INPUT_MIN_VALUE), INPUT_MAX_NET_NODE_SUM);
}

bool check_input_link_sum(long long link_num) {
    return in(link_num, max(0LL, INPUT_MIN_VALUE), INPUT_MAX_LINK_SUM);
}

bool check_input_consumer_sum(long long dest_num) {
    return in(dest_num, max(0LL, INPUT_MIN_VALUE), INPUT_MAX_CONSUMER_NODE_SUM);
}

bool check_input_link_bandwidth(long long bandwidth) {
    return in(bandwidth, INPUT_MIN_LINK_BANDWIDTH, INPUT_MAX_LINK_BANDWIDTH);
}

bool check_input_bandwidth_cost(long long bandwidth_cost) {
    return in(bandwidth_cost, INPUT_MIN_COST_PER_LINK_BANDWIDTH, INPUT_MAX_COST_PER_LINK_BANDWIDTH);
}

bool check_input_server_deploy_cost(long long source_cost) {
    return in(source_cost, INPUT_MIN_SERVER_DEPLOY_COST, INPUT_MAX_SERVER_DEPLOY_COST);
}

bool check_input_consumer_bandwidth_require(long long dest_require) {
    return in(dest_require, INPUT_MIN_CONSUMER_REQUIRE_BANDWIDTH, INPUT_MAX_CONSUMER_REQUIRE_BANDWIDTH);
}

bool check_input_link_sum_per_node(long long link_sum_per_node) {
    return in(link_sum_per_node, 0, INPUT_MAX_LINK_SUM_PER_NODE);
}

bool check_input_class_sum(long long class_sum) {
    return in(class_sum, INPUT_MIN_CLASS_SUM, INPUT_MAX_CLASS_SUM);
}

bool check_input_class_num(long long class_num) {
    return in(class_num, INPUT_MIN_CLASS_SUM - 1, INPUT_MAX_CLASS_SUM - 1);
}

bool check_input_server_output_ability(long long ability) {
    return in(ability, INPUT_MIN_SERVER_OUTPUT_ABILITY, INPUT_MAX_SERVER_OUTPUT_ABILITY);
}

bool check_input_server_hardware_cost(long long cost) {
    return in(cost, INPUT_MIN_SERVER_HARDWARE_COST, INPUT_MAX_SERVER_HARDWARE_COST);
}

bool check_output_class_num(long long class_num) {
    return check_input_class_num(class_num);
}

bool check_output_route_sum(long long sum) {
    return in(sum, OUTPUT_MIN_ROUTE_SUM, OUTPUT_MAX_ROUTE_SUM);
}

bool check_output_node_sum_per_route(long long sum) {
    return in(sum, OUTPUT_MIN_NODE_SUM_PER_ROUTE, OUTPUT_MAX_NODE_SUM_PER_ROUTE);
}

long long link_bandwidth_usage[INPUT_MAX_NET_NODE_SUM + 3][INPUT_MAX_NET_NODE_SUM + 3];
long long cost_per_bandwidth[INPUT_MAX_NET_NODE_SUM + 3][INPUT_MAX_NET_NODE_SUM + 3];
long long bandwidth_require[INPUT_MAX_NET_NODE_SUM + 5];
long long ability_per_net_node[INPUT_MAX_NET_NODE_SUM + 5];
long long deployed_class_id_per_net_node[INPUT_MAX_NET_NODE_SUM + 5];
long long net_node_sum;
long long link_sum;
long long consumer_sum;
//long long source_cost;

bool is_consumer_node[INPUT_MAX_CONSUMER_NODE_SUM + 5];
bool net_consumer_link[INPUT_MAX_NET_NODE_SUM + 3][INPUT_MAX_CONSUMER_NODE_SUM + 3];
long long server_output_ability_per_class[INPUT_MAX_CLASS_SUM + 5];
long long server_hardware_cost_per_class[INPUT_MAX_CLASS_SUM + 5];
long long server_deploy_cost_per_net_node[INPUT_MAX_NET_NODE_SUM + 5];
//long long cost_per_bandwidth[INPUT_MAX_NET_NODE_SUM+3][INPUT_MAX_NET_NODE_SUM+3];

bool check_input_net_node_num(long long net_node_num) {
    return in(net_node_num, INPUT_MIN_VALUE, net_node_sum - 1);
}

bool next_char(FILE *fp) {
    char c;
    bool has_newline = false;
    while (c = (char) (getc(fp))) {
        if (c == ' ' || c == '\t') {
            continue;
        } else if (c == '\n' || c == '\r') {
            has_newline = true;
            continue;
        } else {
            fseek(fp, -1, SEEK_CUR);
            return has_newline;
        }
    }
    return has_newline;
}

long long result = 0;

bool read_input(FILE *fp) {
    if (fscanf(fp, "%lld%lld%lld", &net_node_sum, &link_sum, &consumer_sum) != 3) {
        printf("lack parameter.\n");
        return false;
    }
    if (!(check_input_net_node_sum(net_node_sum) && check_input_link_sum(link_sum)
          && check_input_consumer_sum(consumer_sum))) {
        printf("check 3 parameters error on first line.\n");
        return false;
    }

    long long class_id, output_ability, hardware_cost;
    long long net_node_id, deploy_cost;
    while (true) {
        fscanf(fp, "%lld%lld", &class_id, &output_ability);
        if (next_char(fp)) {
            net_node_id = class_id;
            deploy_cost = output_ability;
            break;
        } else {
            fscanf(fp, "%lld", &hardware_cost);
        }
//        printf("## class id is %lld, output ability is %lld, hardware cost is %lld.\n", class_id, output_ability,
//               hardware_cost);
        if (!check_input_class_num(class_id)) {
            printf("error: class id is %lld.\n", class_id);
            return false;
        }
        if (!check_input_server_output_ability(output_ability)) {
            printf("error: output ability is %lld.\n", output_ability);
            return false;
        }
        if (!check_input_server_hardware_cost(hardware_cost)) {
            printf("error: hardware cost is %lld.\n", hardware_cost);
        }
        server_output_ability_per_class[class_id] = output_ability;
        server_hardware_cost_per_class[class_id] = hardware_cost;
    }

    if (!check_input_net_node_num(net_node_id)) {
        printf("error: net node id is %lld.\n", net_node_id);
        return false;
    }
    if (!check_input_server_deploy_cost(deploy_cost)) {
        printf("error: deploy cost is %lld.\n", deploy_cost);
        return false;
    }
    server_deploy_cost_per_net_node[net_node_id] = deploy_cost;

    for (long long i = 0; i < net_node_sum - 1; ++i) {
        fscanf(fp, "%lld%lld", &net_node_id, &deploy_cost);
        if (!check_input_net_node_num(net_node_id)) {
            printf("error: net node id is %lld.\n", net_node_id);
            return false;
        }
        if (!check_input_server_deploy_cost(deploy_cost)) {
            printf("error: deploy cost is %lld.\n", deploy_cost);
            return false;
        }
        if (server_deploy_cost_per_net_node[net_node_id] != 0) {
            printf("error: net node %lld's deploy cost appears twice.\n", net_node_id);
            return false;
        }
        server_deploy_cost_per_net_node[net_node_id] = deploy_cost;
    }

    long long u, v, bw, bw_cost;
    for (long long i = 0; i < link_sum; ++i) {
        if (fscanf(fp, "%lld%lld%lld%lld", &u, &v, &bw, &bw_cost) != 4) {
            printf("error: lack link's information.\n");
            return false;
        }
        if (!(check_input_link_bandwidth(bw) && check_input_bandwidth_cost(bw_cost))) {
            printf("error: bandwidth is %lld, and cost per bandwidth is %lld.\n", bw, bw_cost);
            return false;
        }
        if (link_bandwidth_usage[u][v] != 0 || link_bandwidth_usage[v][u] != 0) {
            printf("error: there are not only one link on %lld to %lld.\n", u, v);
            return false;
        }
        link_bandwidth_usage[u][v] = bw;
        link_bandwidth_usage[v][u] = bw;
        cost_per_bandwidth[u][v] = bw_cost;
        cost_per_bandwidth[v][u] = bw_cost;
    }
    long long require;
    for (long long i = 0; i < consumer_sum; ++i) {
        if (fscanf(fp, "%lld%lld%lld", &u, &v, &require) != 3) {
            printf("error: lack require's information.\n");
            return false;
        }
        if (!check_input_consumer_bandwidth_require(require)) {
            printf("error: consumer bandwidth require is %lld.\n", require);
            return false;
        }
        if (is_consumer_node[u]) {
            printf("error: consumer node %lld has appeared.\n", u);
            return false;
        }
        if (bandwidth_require[v] != 0) {
            printf("error: net node %lld has appeared.\n", v);
            return false;
        }
        if (net_consumer_link[v][u]) {
            printf("error: link for net node %lld to consumer node %lld has appeared.\n", v, u);
            return false;
        }
        is_consumer_node[u] = true;
        net_consumer_link[v][u] = true;
        bandwidth_require[v] += require;
    }
    printf("read input is OK.\n");
    return true;
}

char buffer[INPUT_MAX_NET_NODE_SUM * 10 + 5];
char sprintf_buffer[256];
long long plan_link_sum;

long long get_len(long long number) {
    sprintf(sprintf_buffer, "%lld", number);
    return (long long) strlen(sprintf_buffer);
}

bool read_result(FILE *fp) {
    long long line_number = 1;
    if (fscanf(fp, "%lld", &plan_link_sum) != 1) {
        printf("error: lack number in result file.\n");
        return false;
    }
    if (!check_output_route_sum(plan_link_sum)) {
        printf("error: route number is %lld.\n", plan_link_sum);
        return false;
    }
    if (fgetc(fp) == '\n') {
        ++line_number;
        if (fgetc(fp) == '\n') {
            ++line_number;
        } else {
            printf("error: format error on result line %lld.\n", line_number);
            return false;
        }
    } else {
        printf("error: format error on result line %lld.\n", line_number);
        return false;
    }
    for (long long i = 0; i < plan_link_sum; ++i) {
        memset(buffer, 0, sizeof(buffer));
        fgets(buffer, (int) (INPUT_MAX_NET_NODE_SUM * 10), fp);
        char *buffer_p = buffer;
        long long num;
        vector<long long> read_list;
        while (sscanf(buffer_p, "%lld", &num) == 1) {
            read_list.push_back(num);
            buffer_p += get_len(num) + 1;
        }
        long long class_id = *(read_list.end() - 1);
        if (!check_input_class_num(class_id)) {
            printf("error: on result line %lld, class id is %lld.\n", line_number, class_id);
            return false;
        }
        long long bandwidth_cost = *(read_list.end() - 2);
        if (bandwidth_cost <= 0) {
            printf("error: on result line %lld, bandwidth cost is %lld.\n", line_number, bandwidth_cost);
            return false;
        }
        long long consumer_id = *(read_list.end() - 3);
        if (!is_consumer_node[consumer_id]) {
            printf("error: on result line %lld, %lld is not a consumer node.\n", line_number, consumer_id);
            return false;
        }
        long long end_net_node = *(read_list.end() - 4);
        if (!net_consumer_link[end_net_node][consumer_id]) {
            printf("error: net node %lld has no link to consumer node %lld, but appears on line %lld in result file.\n",
                   end_net_node, consumer_id, line_number);
            return false;
        }
        long long server_net_node = read_list[0];
        if (deployed_class_id_per_net_node[server_net_node] != -1 &&
            class_id != deployed_class_id_per_net_node[server_net_node]) {
            printf("error: on result line %lld, net node %lld has deployed class %lld's server, but now plan to deploy a new class %lld server",
                   line_number, server_net_node, deployed_class_id_per_net_node[server_net_node], class_id);
            return false;
        }

        if (deployed_class_id_per_net_node[server_net_node] == -1) {
            deployed_class_id_per_net_node[server_net_node] = class_id;
            ability_per_net_node[server_net_node] = server_output_ability_per_class[class_id];
            result += server_deploy_cost_per_net_node[server_net_node];
            result += server_hardware_cost_per_class[class_id];
        }

        ability_per_net_node[server_net_node] -= bandwidth_cost;

        long long u = *read_list.begin();
        long long v;
        for (size_t j = 1; j < read_list.size() - 3; ++j) {
            v = read_list[j];
            link_bandwidth_usage[u][v] -= bandwidth_cost;
            result += cost_per_bandwidth[u][v] * bandwidth_cost;
            u = v;
        }
        bandwidth_require[end_net_node] -= bandwidth_cost;
        ++line_number;
    }
    printf("read result is OK.\n");
    return true;
}

bool check_result() {
    for (long long i = 0; i < net_node_sum; ++i) {
        if (bandwidth_require[i] != 0) {
            printf("net node %lld require is %lld, not zero.\n", i, bandwidth_require[i]);
            return false;
        }
    }
    for (long long i = 0; i < net_node_sum; ++i) {
        if (ability_per_net_node[i] < 0) {
            printf("server on net node %lld's remain output ability is %lld, less than zero.\n", i,
                   ability_per_net_node[i]);
            return false;
        }
    }
    for (long long i = 0; i < net_node_sum; ++i) {
        for (long long j = 0; j < net_node_sum; ++j) {
            if (link_bandwidth_usage[i][j] < 0) {
                printf("bandwidth of link %lld to %lld is remain %lld, less than zero.\n", i, j,
                       link_bandwidth_usage[i][j]);
                return false;
            }
        }
    }
    return true;
}

void init() {
    memset(deployed_class_id_per_net_node, -1LL, sizeof(deployed_class_id_per_net_node));
    if (deployed_class_id_per_net_node[816] != -1) {
        printf("Warning: init value is %lld.\n", deployed_class_id_per_net_node[816]);
    }
}

int main(int argc, char *argv[]) {
    printf("%d\n", (-1)^1);
    init();
    if (argc != 3) {
        printf("arguments error.\n");
        return 1;
    }
    char *input_file = argv[1];
    char *result_file = argv[2];

    FILE *input_fp = fopen(input_file, "r");
    if (!check_fp(input_fp)) {
        printf("open input file with error.\n");
        return 1;
    }


    if (!read_input(input_fp)) {
        printf("input error.\n");
        return 1;
    }

    FILE *result_fp = fopen(result_file, "r");
    if (!check_fp(result_fp)) {
        printf("open result file with error.\n");
        return 1;
    }

    if (!read_result(result_fp)) {
        printf("result error.\n");
        return 1;
    }
    if (!check_result()) {
        printf("result error.\n");
        return 1;
    }

    printf("Accepted!\n");
    printf("Final result is %lld.\n", result);

    return 0;
}